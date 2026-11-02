import enum
from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

if TYPE_CHECKING:
    from app.models import Application


class MaritalStatus(str, enum.Enum):
    SINGLE = "single"
    MARRIED = "married"


MARITALSTATUS_LABELS: dict[MaritalStatus, str] = {
    MaritalStatus.SINGLE: "Не женат/Не замужем",
    MaritalStatus.MARRIED: "Женат/Замужем",
}


class Education(str, enum.Enum):
    NE = "NE"
    BGE = "BGE"
    SE = "SE"
    SVE = "SVE"
    HE = "HE"
    SHE = "SHE"
    AD = "AD"


EDUCATION_LABELS: dict[Education, str] = {
    Education.NE: "Нет образования",
    Education.BGE: "Основное общее",
    Education.SE: "Среднее",
    Education.SVE: "Среднее специальное",
    Education.HE: "Высшее",
    Education.SHE: "Второе высшее",
    Education.AD: "Учёная степень",
}


class Questionnaire(Base):
    __tablename__ = "questionnaires"

    id: Mapped[int] = mapped_column(primary_key=True)
    application_id: Mapped[int] = mapped_column(
        ForeignKey("applications.id"), nullable=False, unique=True
    )

    car_own_flg: Mapped[bool] = mapped_column(Boolean, default=False)
    car_type_flg: Mapped[bool] = mapped_column(Boolean, default=False)

    marital_status: Mapped[MaritalStatus] = mapped_column(
        Enum(
            MaritalStatus,
            native_enum=False,
            values_callable=lambda e: [m.value for m in e],
        ),
        nullable=False,
    )
    dependents: Mapped[int] = mapped_column(nullable=False, default=0)

    education: Mapped[Education] = mapped_column(
        Enum(
            Education, native_enum=False, values_callable=lambda e: [m.value for m in e]
        ),
        nullable=False,
    )
    income: Mapped[int] = mapped_column(nullable=False)
    extra_income: Mapped[int] = mapped_column(default=0, nullable=False)

    has_house: Mapped[bool] = mapped_column(Boolean, default=False)
    has_apartment: Mapped[bool] = mapped_column(Boolean, default=False)

    application: Mapped["Application"] = relationship(back_populates="questionnaire")
