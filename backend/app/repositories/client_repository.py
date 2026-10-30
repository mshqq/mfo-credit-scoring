from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.client import Client
from app.schemas.client import ClientCreate


class ClientRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_all(self) -> list[Client] | None:
        statement = select(Client)
        return list(self.db.scalars(statement).all())

    def get_by_id(self, client_id: int) -> Client | None:
        return self.db.get(Client, client_id)

    def create(self, client_data: ClientCreate) -> Client:
        new_client = Client(**client_data.model_dump())

        self.db.add(new_client)
        self.db.commit()
        self.db.refresh(new_client)

        return new_client
