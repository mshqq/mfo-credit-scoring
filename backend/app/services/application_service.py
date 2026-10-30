from sqlalchemy.orm import Session

from app.schemas.applicaion import ApplicationRead


class ApplicationService:
    def __init__(self, db: Session) -> None:
        self.repository = ApplicationService(db)

    def get_by_id(self, application_id: int) -> ApplicationRead | None:
        application = self.repository.get_by_id(application_id)
        if application is None:
            return None
        return ApplicationRead.model_validate(application)

    def get_all_applications(self) -> list[ApplicationRead] | None:
        applications = self.repository.get_all_applications()
        if applications is None:
            return None
        return [ApplicationRead.model_validate(a) for a in applications]
