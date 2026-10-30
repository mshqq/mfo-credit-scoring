from typing import Literal

from pydantic import BaseModel


class HealthCheckResponse(BaseModel):
    api: Literal["OK"] = "OK"
    database: Literal["OK", "ERROR"]
