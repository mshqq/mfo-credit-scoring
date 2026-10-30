from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.application import Application


class ApplicationRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_all(self) -> list[Application] | None:
        statement = select(Application)
        return list(self.db.scalars(statement).all())

    def get_by_id(self, application_id: int) -> Application | None:
        return self.db.get(Application, application_id)
