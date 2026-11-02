import enum
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, Enum, Float, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

if TYPE_CHECKING:
    from app.models import Application


class Decision(str, enum.Enum):
    APPROVE = "approve"
    REJECT = "reject"
    MANUAL_REVIEW = "manual_review"


DECISION_LABELS: dict[Decision, str] = {
    Decision.APPROVE: "Выдать",
    Decision.REJECT: "Отказать",
    Decision.MANUAL_REVIEW: "На ручное рассмотрение",
}


class ScoringResult(Base):
    __tablename__ = "scoring_results"

    id: Mapped[int] = mapped_column(primary_key=True)
    application_id: Mapped[int] = mapped_column(
        ForeignKey("applications.id"), nullable=False, unique=True
    )

    probability: Mapped[float] = mapped_column(Float, nullable=False)
    decision: Mapped[Decision] = mapped_column(
        Enum(
            Decision,
            native_enum=False,
            length=14,
            values_callable=lambda e: [m.value for m in e],
        ),
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    application: Mapped["Application"] = relationship(back_populates="scoring_result")
