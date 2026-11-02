from pydantic import BaseModel, ConfigDict, Field

from app.models.questionnaire import Education, MaritalStatus


class QuestionnaireCreate(BaseModel):
    car_own_flg: bool = False
    car_type_flg: bool = False

    marital_status: MaritalStatus
    dependents: int = Field(default=0, ge=0, le=20)
    education: Education

    income: int = Field(ge=0)
    extra_income: int = Field(default=0, ge=0)

    has_house: bool = False
    has_apartment: bool = False


class QuestionnaireRead(QuestionnaireCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
    application_id: int
