from datetime import date, datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field, field_serializer, field_validator

from app.models.client import Education, Gender, MaritalStatus


def _mask(value: str, keep: int = 4) -> str:
    return "*" * max(len(value) - keep, 0) + value[-keep:]


class ClientBase(BaseModel):
    first_name: str = Field(min_length=1, max_length=100)
    last_name: str = Field(min_length=1, max_length=100)
    middle_name: str | None = Field(default=None, min_length=1, max_length=100)

    phone: str
    gender: Gender
    birth_date: date

    passport: str
    registration_address: str
    snils: str
    inn: str

    car_own_flg: bool = False
    car_type_flg: bool = False

    marital_status: MaritalStatus
    dependents: int = Field(default=0, ge=0, le=20)
    education: Education

    income: int = Field(ge=0)
    extra_income: int = Field(default=0, ge=0)

    has_house: bool = False
    has_apartment: bool = False

    amount: int = Field(gt=0)
    term: int = Field(gt=0)
    rate: Decimal = Field(ge=0, max_digits=5, decimal_places=2)

    @field_validator("birth_date")
    def validate_age(cls, v: date) -> date:
        today = date.today()
        age = today.year - v.year - ((today.month, today.day) < (v.month, v.day))
        if age < 18:
            raise ValueError("Клиенту должно быть не менее 18 лет")
        if age > 100:
            raise ValueError("Проверьте дату рождения")
        return v


class ClientCreate(ClientBase):
    pass


class ClientRead(ClientBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime

    @field_serializer("passport")
    def mask_passport(self, v: str) -> str:
        return _mask(v, 4)

    @field_serializer("snils")
    def mask_snils(self, v: str) -> str:
        return _mask(v, 2)

    @field_serializer("inn")
    def mask_inn(self, v: str) -> str:
        return _mask(v, 4)
