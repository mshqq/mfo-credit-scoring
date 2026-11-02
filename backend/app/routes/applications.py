from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies import get_current_user
from app.models import User
from app.schemas.application import ApplicationCreate, ApplicationRead
from app.services.application_service import ApplicationService, ClientNotFoundError

router = APIRouter(
    prefix="/api/applications",
    tags=["applications"],
    dependencies=[Depends(get_current_user)],
)


@router.get("/", response_model=list[ApplicationRead], status_code=status.HTTP_200_OK)
def get_applications(db: Session = Depends(get_db)):
    service = ApplicationService(db)
    return service.get_all_applications()


@router.get(
    "/{application_id}", response_model=ApplicationRead, status_code=status.HTTP_200_OK
)
def get_application(application_id: int, db: Session = Depends(get_db)):
    service = ApplicationService(db)
    application = service.get_by_id(application_id)
    if application is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Заявка не найдена"
        )
    return application


@router.post("/", response_model=ApplicationRead, status_code=status.HTTP_201_CREATED)
def create_application(
    data: ApplicationCreate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    service = ApplicationService(db)

    try:
        return service.create_application(data, user.id)
    except ClientNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)
        ) from exc
