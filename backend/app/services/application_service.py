from sqlalchemy.orm import Session

from app.repositories.application_repository import ApplicationRepository
from app.repositories.client_repository import ClientRepository
from app.schemas.application import ApplicationCreate, ApplicationRead


class ClientNotFoundError(Exception):
    pass


class ApplicationService:
    def __init__(self, db: Session) -> None:
        self.repository = ApplicationRepository(db)
        self.client_repository = ClientRepository(db)

    def get_by_id(self, application_id: int) -> ApplicationRead | None:
        application = self.repository.get_by_id(application_id)
        if application is None:
            return None
        return ApplicationRead.model_validate(application)

    def get_all_applications(self) -> list[ApplicationRead] | None:
        applications = self.repository.get_all()
        if applications is None:
            return None
        return [ApplicationRead.model_validate(a) for a in applications]

    def create_application(
        self, application_data: ApplicationCreate, user_id: int
    ) -> ApplicationRead:
        client = self.client_repository.get_by_id(application_data.client_id)
        if client is None:
            raise ClientNotFoundError("Клиент не найден")

        application = self.repository.create(application_data, user_id)
        return ApplicationRead.model_validate(application)
