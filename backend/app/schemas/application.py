from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field

from app.schemas.questionnaire import QuestionnaireCreate, QuestionnaireRead


class ApplicationBase(BaseModel):
    client_id: int = Field(gt=0)
    amount: Decimal = Field(gt=Decimal(0), max_digits=12, decimal_places=2)
    term: int = Field(gt=0)
    rate: Decimal = Field(ge=Decimal(0), max_digits=5, decimal_places=2)


class ApplicationCreate(ApplicationBase):
    questionnaire: QuestionnaireCreate


class ApplicationRead(ApplicationBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    created_at: datetime
    questionnaire: QuestionnaireRead | None = None
