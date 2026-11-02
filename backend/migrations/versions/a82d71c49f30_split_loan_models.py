"""Split clients and applications into seven entities, preserving existing data.

Revision ID: a82d71c49f30
Revises: 51e83404f0c0
"""

from alembic import op
import sqlalchemy as sa

revision = "a82d71c49f30"
down_revision = "51e83404f0c0"
branch_labels = None
depends_on = None

NAMING = {"uq": "uq_%(table_name)s_%(column_0_name)s"}
QUESTIONNAIRE_FIELDS = (
    "car_own_flg", "car_type_flg", "marital_status", "dependents",
    "education", "income", "extra_income", "has_house", "has_apartment",
)
TERMS = ("amount", "term", "rate")


def questionnaire_columns():
    return [
        sa.Column("car_own_flg", sa.Boolean(), nullable=False),
        sa.Column("car_type_flg", sa.Boolean(), nullable=False),
        sa.Column("marital_status", sa.Enum(
            "single", "married", name="maritalstatus", native_enum=False
        ), nullable=False),
        sa.Column("dependents", sa.Integer(), nullable=False),
        sa.Column("education", sa.Enum(
            "NE", "BGE", "SE", "SVE", "HE", "SHE", "AD",
            name="education", native_enum=False
        ), nullable=False),
        sa.Column("income", sa.Integer(), nullable=False),
        sa.Column("extra_income", sa.Integer(), nullable=False),
        sa.Column("has_house", sa.Boolean(), nullable=False),
        sa.Column("has_apartment", sa.Boolean(), nullable=False),
    ]


def terms_columns():
    return [
        sa.Column("amount", sa.Numeric(12, 2), nullable=False),
        sa.Column("term", sa.Integer(), nullable=False),
        sa.Column("rate", sa.Numeric(5, 2), nullable=False),
    ]


def decision_column():
    return sa.Column("decision", sa.Enum(
        "approve", "reject", "manual_review", name="decision",
        native_enum=False, length=14
    ), nullable=False)


def created_at_column():
    return sa.Column("created_at", sa.DateTime(timezone=True),
                     server_default=sa.func.now(), nullable=False)


def require_empty(query, message):
    if op.get_bind().execute(sa.text(query)).first() is not None:
        raise RuntimeError(message)


def upgrade():
    # These clients have questionnaire data but no application to attach it to.
    # Abort before changing anything instead of silently discarding their data.
    require_empty(
        "SELECT c.id FROM clients c LEFT JOIN applications a ON a.client_id = c.id "
        "WHERE a.id IS NULL",
        "Cannot migrate clients without applications: link them to applications first.",
    )
    unique_name = next(
        constraint["name"] or "uq_applications_client_id"
        for constraint in sa.inspect(op.get_bind()).get_unique_constraints("applications")
        if constraint["column_names"] == ["client_id"]
    )
    with op.batch_alter_table("applications", naming_convention=NAMING) as batch:
        for column in terms_columns():
            column.nullable = True
            batch.add_column(column)
        batch.drop_constraint(unique_name, type_="unique")

    op.execute(sa.text(
        "UPDATE applications SET " + ", ".join(
            f"{name} = (SELECT c.{name} FROM clients c WHERE c.id = applications.client_id)"
            for name in TERMS
        )
    ))
    with op.batch_alter_table("applications") as batch:
        for column in terms_columns():
            batch.alter_column(column.name, existing_type=column.type, nullable=False)

    op.create_table(
        "questionnaires",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("application_id", sa.Integer(), sa.ForeignKey("applications.id"),
                  nullable=False, unique=True),
        *questionnaire_columns(),
    )
    op.create_table(
        "scoring_results",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("application_id", sa.Integer(), sa.ForeignKey("applications.id"),
                  nullable=False, unique=True),
        sa.Column("probability", sa.Float(), nullable=False),
        decision_column(), created_at_column(),
    )
    fields = ", ".join(QUESTIONNAIRE_FIELDS)
    op.execute(sa.text(
        f"INSERT INTO questionnaires (application_id, {fields}) "
        "SELECT a.id, " + ", ".join(f"c.{name}" for name in QUESTIONNAIRE_FIELDS) +
        " FROM applications a JOIN clients c ON c.id = a.client_id"
    ))
    op.execute(sa.text(
        "INSERT INTO scoring_results (application_id, probability, decision, created_at) "
        "SELECT id, probability, decision, created_at FROM applications"
    ))
    # Remove old columns before adding tables referencing applications: SQLite
    # batch operations recreate the parent table.
    with op.batch_alter_table("applications") as batch:
        batch.drop_column("probability")
        batch.drop_column("decision")
    with op.batch_alter_table("clients") as batch:
        for name in (*QUESTIONNAIRE_FIELDS, *TERMS):
            batch.drop_column(name)

    op.create_table(
        "loans",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("application_id", sa.Integer(), sa.ForeignKey("applications.id"),
                  nullable=False),
        *terms_columns(),
        sa.Column("issued_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("due_date", sa.Date(), nullable=False),
        sa.Column("status", sa.Enum("active", "closed", name="loanstatus",
                                    native_enum=False), nullable=False),
        created_at_column(),
    )
    op.create_table(
        "payments",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("loan_id", sa.Integer(), sa.ForeignKey("loans.id"), nullable=False),
        sa.Column("amount", sa.Numeric(12, 2), nullable=False),
        created_at_column(),
    )


def downgrade():
    # The old schema cannot represent these records. Do not delete them silently.
    require_empty("SELECT id FROM loans", "Cannot downgrade while loans exist.")
    require_empty("SELECT id FROM payments", "Cannot downgrade while payments exist.")
    require_empty(
        "SELECT client_id FROM applications GROUP BY client_id HAVING COUNT(*) > 1",
        "Cannot downgrade clients with multiple applications.",
    )
    require_empty(
        "SELECT c.id FROM clients c LEFT JOIN applications a ON a.client_id = c.id "
        "LEFT JOIN questionnaires q ON q.application_id = a.id "
        "LEFT JOIN scoring_results s ON s.application_id = a.id "
        "WHERE a.id IS NULL OR q.id IS NULL OR s.id IS NULL",
        "Cannot downgrade: each client needs an application, questionnaire and score.",
    )
    with op.batch_alter_table("clients") as batch:
        for column in [*questionnaire_columns(), *terms_columns()]:
            column.nullable = True
            batch.add_column(column)
    with op.batch_alter_table("applications") as batch:
        batch.add_column(sa.Column("probability", sa.Float(), nullable=True))
        column = decision_column()
        column.nullable = True
        batch.add_column(column)

    op.execute(sa.text(
        "UPDATE clients SET " + ", ".join(
            f"{name} = (SELECT q.{name} FROM questionnaires q "
            "JOIN applications a ON a.id = q.application_id WHERE a.client_id = clients.id)"
            for name in QUESTIONNAIRE_FIELDS
        ) + ", " + ", ".join(
            f"{name} = (SELECT a.{name} FROM applications a WHERE a.client_id = clients.id)"
            for name in TERMS
        )
    ))
    op.execute(sa.text(
        "UPDATE applications SET " + ", ".join(
            f"{name} = (SELECT s.{name} FROM scoring_results s "
            "WHERE s.application_id = applications.id)"
            for name in ("probability", "decision")
        )
    ))
    op.drop_table("payments")
    op.drop_table("loans")
    op.drop_table("scoring_results")
    op.drop_table("questionnaires")
    with op.batch_alter_table("applications", naming_convention=NAMING) as batch:
        batch.alter_column("probability", existing_type=sa.Float(), nullable=False)
        batch.alter_column("decision", existing_type=decision_column().type, nullable=False)
        for name in TERMS:
            batch.drop_column(name)
        batch.create_unique_constraint("uq_applications_client_id", ["client_id"])
    with op.batch_alter_table("clients") as batch:
        for column in [*questionnaire_columns(), *terms_columns()]:
            batch.alter_column(column.name, existing_type=column.type, nullable=False)
