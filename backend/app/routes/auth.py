from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.dependencies import get_current_user
from app.models import User
from app.schemas.auth import LoginRequest
from app.schemas.user import UserResponse
from app.services.auth_service import AuthenticationError, AuthService

from ..database import get_db
from ..schemas.auth import TokenResponse

router = APIRouter(prefix="/api/auth", tags=["auth"])


@router.post("/login", response_model=TokenResponse, status_code=status.HTTP_200_OK)
def login_user(data: LoginRequest, db: Session = Depends(get_db)) -> TokenResponse:
    service = AuthService(db)
    try:
        token = service.login(str(data.email), data.password)
    except AuthenticationError as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail=str(exc)
        ) from exc

    return TokenResponse(access_token=token)


@router.get("/me", response_model=UserResponse)
def get_me(user: User = Depends(get_current_user)):
    return user
