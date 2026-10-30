from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    first_name: str = Field(max_length=255)
    last_name: str = Field(max_length=255)
    middle_name: str = Field(max_length=255)

    password: str = Field(min_length=8, max_length=128)


class UserResponse(UserBase):
    id: int
    first_name: str
    last_name: str
    middle_name: str

    created_at: datetime
    is_active: bool

    model_config = ConfigDict(from_attributes=True)
