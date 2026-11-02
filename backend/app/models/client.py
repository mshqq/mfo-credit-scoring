import enum
from datetime import date, datetime
from typing import TYPE_CHECKING

from sqlalchemy import Date, DateTime, Enum, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

if TYPE_CHECKING:
    from app.models import Application


class Gender(str, enum.Enum):
    MALE = "male"
    FEMALE = "female"


GENDER_LABELS: dict[Gender, str] = {Gender.MALE: "Мужской", Gender.FEMALE: "Женский"}


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

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    applications: Mapped[list["Application"]] = relationship(
        back_populates="client"
    )
