import enum
from datetime import date, datetime
from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Date, DateTime, Enum, Numeric, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

if TYPE_CHECKING:
    from app.models import Application


class Gender(str, enum.Enum):
    MALE = "male"
    FEMALE = "female"


GENDER_LABELS: dict[Gender, str] = {Gender.MALE: "Мужской", Gender.FEMALE: "Женский"}


class MaritalStatus(str, enum.Enum):
    SINGLE = "single"
    MARRIED = "married"


MARITIALSTATUS_LABELS: dict[MaritalStatus, str] = {
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


class Client(Base):
    __tablename__ = "clients"

    id: Mapped[int] = mapped_column(primary_key=True)

    first_name: Mapped[str] = mapped_column(String(100), nullable=False)
    last_name: Mapped[str] = mapped_column(String(100), nullable=False)
    middle_name: Mapped[str | None] = mapped_column(String(100), nullable=True)

    phone: Mapped[str] = mapped_column(String(20), nullable=False)

    gender: Mapped[Gender] = mapped_column(
        Enum(
            Gender,
            native_enum=False,
            values_callable=lambda e: [m.value for m in e],
        ),
        nullable=False,
    )
    birth_date: Mapped[date] = mapped_column(Date(), nullable=False)

    passport: Mapped[str] = mapped_column(String(20), nullable=False)
    registration_address: Mapped[str] = mapped_column(Text, nullable=False)
    snils: Mapped[str] = mapped_column(String(12), nullable=False)
    inn: Mapped[str] = mapped_column(String(12), nullable=False)

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

    amount: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    term: Mapped[int] = mapped_column(nullable=False)
    rate: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    application: Mapped["Application | None"] = relationship(
        "Application", back_populates="client", uselist=False, lazy="joined"
    )
