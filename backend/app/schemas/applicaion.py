from datetime import datetime

from pydantic import BaseModel, Field

from app.models.application import Decision


class ApplicationCreate(BaseModel):
    client_id: int = Field(gt=0)


class ApplicationRead(BaseModel):
    id: int
    user_id: int | None
    client_id: int
    decision: Decision
    created_at: datetime
