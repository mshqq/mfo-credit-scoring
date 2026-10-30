from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.dependencies import get_current_user

from ..database import get_db
from ..schemas.user import UserResponse
from ..services.user_service import UserService

router = APIRouter(
    prefix="/api/users", tags=["users"], dependencies=[Depends(get_current_user)]
)


@router.get("/", response_model=list[UserResponse], status_code=status.HTTP_200_OK)
def get_users(db: Session = Depends(get_db)):
    service = UserService(db)
    return service.get_all_users()


@router.get("/{user_id}", response_model=UserResponse, status_code=status.HTTP_200_OK)
def get_user(user_id: int, db: Session = Depends(get_db)):
    service = UserService(db)
    user = service.get_user_by_id(user_id)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found",
        )

    return user
