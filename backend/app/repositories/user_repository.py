from sqlalchemy import select
from sqlalchemy.orm import Session

from ..models.user import User
from ..schemas.user import UserCreate


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> list[User]:
        statement = select(User)
        return list(self.db.scalars(statement).all())

    def get_by_id(self, user_id: int) -> User | None:
        statement = select(User).where(User.id == user_id)
        return self.db.scalars(statement).first()

    def get_by_email(self, email: str) -> User | None:
        statement = select(User).where(User.email == email)
        return self.db.scalars(statement).first()

    def create(self, user_data: UserCreate) -> User:
        db_user = User(email=str(user_data.email))
        db_user.set_password(user_data.password)

        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)

        return db_user
