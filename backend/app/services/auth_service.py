from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.security import create_access_token


class AuthenticationError(Exception):
    pass


class AuthService:
    def __init__(self, db: Session):
        self.repository = UserRepository(db)

    def login(self, email: str, password: str) -> str:
        user: User | None = self.repository.get_by_email(email)

        if user is None or not user.check_password(password):
            raise AuthenticationError("Неверный email или пароль")

        if not user.is_active:
            raise AuthenticationError("Пользователь отключён")

        return create_access_token(user.id)
