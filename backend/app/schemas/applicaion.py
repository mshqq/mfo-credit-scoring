from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field

class ApplicationCreate(BaseModel):
    client_id: int = Field(gt=0)
    amount: Decimal = Field(gt=0, max_digits=12, decimal_places=2)
    term: int = Field(gt=0)
    rate: Decimal = Field(ge=0, max_digits=5, decimal_places=2)


class ApplicationRead(ApplicationCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    created_at: datetime
