from sqlalchemy.orm import Session

from app.repositories.client_repository import ClientRepository


class ScoringService:
    def __init__(self, db: Session) -> None:
        self.repository = ClientRepository(db)

    def get_score(self, client_id: int):
        client = self.repository.get_by_id(client_id)
        if client is None:
            return None

        return client
