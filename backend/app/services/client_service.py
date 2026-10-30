from sqlalchemy.orm import Session

from app.models.client import Client
from app.repositories.client_repository import ClientRepository
from app.schemas.client import ClientCreate, ClientRead


class ClientService:
    def __init__(self, db: Session):
        self.repository = ClientRepository(db)

    def get_by_id(self, client_id: int) -> ClientRead | None:
        client = self.repository.get_by_id(client_id)
        if client is None:
            return None
        return ClientRead.model_validate(client)

    def get_all_clients(self) -> list[ClientRead] | None:
        clients = self.repository.get_all()
        if clients is None:
            return None
        return [ClientRead.model_validate(c) for c in clients]

    def create_client(self, client_data: ClientCreate) -> ClientRead:
        client: Client = self.repository.create(client_data)
        return ClientRead.model_validate(client)
