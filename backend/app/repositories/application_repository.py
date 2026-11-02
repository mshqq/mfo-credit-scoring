from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app.models import Questionnaire
from app.models.application import Application
from app.schemas.application import ApplicationCreate


class ApplicationRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_all(self) -> list[Application] | None:
        statement = select(Application)
        return list(self.db.scalars(statement).all())

    def get_by_id(self, application_id: int) -> Application | None:
        return self.db.get(Application, application_id)

    def create(self, application_data: ApplicationCreate, user_id: int) -> Application:
        application = Application(
            **application_data.model_dump(exclude={"questionnaire"}), user_id=user_id
        )
        application.questionnaire = Questionnaire(
            **application_data.questionnaire.model_dump()
        )

        try:
            self.db.add(application)
            self.db.commit()
        except SQLAlchemyError:
            self.db.rollback()
            raise

        self.db.refresh(application)
        return application
