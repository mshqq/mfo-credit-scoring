from fastapi import APIRouter, Depends, Response, status
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.health import HealthCheckResponse

router = APIRouter(prefix="/api/health", tags=["health"])


@router.get(
    "/",
    response_model=HealthCheckResponse,
    responses={503: {"model": HealthCheckResponse}},
    status_code=status.HTTP_200_OK,
)
def health_check(response: Response, db: Session = Depends(get_db)):
    try:
        database_ok = db.execute(text("SELECT 1")).scalar_one() == 1
    except SQLAlchemyError:
        database_ok = False

    if not database_ok:
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE

    return HealthCheckResponse(database="OK" if database_ok else "ERROR")
