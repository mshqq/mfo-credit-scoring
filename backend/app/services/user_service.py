from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from ..models.user import User
from ..repositories.user_repository import UserRepository
from ..schemas.user import UserCreate, UserResponse


class EmailAlreadyExistsError(Exception):
    pass


class UserService:
    def __init__(self, db: Session):
        self.repository = UserRepository(db)

    def get_all_users(self) -> list[UserResponse]:
        users: list[User] = self.repository.get_all()
        return [UserResponse.model_validate(u) for u in users]

    def get_user_by_id(self, user_id: int) -> UserResponse | None:
        user: User | None = self.repository.get_by_id(user_id)

        if user is None:
            return None

        return UserResponse.model_validate(user)

    def get_user_by_email(self, email: str) -> UserResponse | None:
        user: User | None = self.repository.get_by_email(email)

        if user is None:
            return None

        return UserResponse.model_validate(user)

    def create_user(self, user_data: UserCreate) -> UserResponse:
        email = str(user_data.email)

        existing_user: UserResponse | None = self.get_user_by_email(email)
        if existing_user is not None:
            raise EmailAlreadyExistsError("Пользователь с таким Email уже существует")

        try:
            user: User = self.repository.create(user_data)
        except IntegrityError as exc:
            self.repository.db.rollback()
            raise EmailAlreadyExistsError(
                "Пользователь с таким Email уже существует"
            ) from exc

        return UserResponse.model_validate(user)
