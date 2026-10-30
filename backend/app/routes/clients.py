from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies import get_current_user
from app.schemas.client import ClientCreate, ClientRead
from app.services.client_service import ClientService
from app.services.scoring_service import ScoringService

router = APIRouter(
    prefix="/api/clients", tags=["clients"], dependencies=[Depends(get_current_user)]
)


@router.get("/", response_model=list[ClientRead], status_code=status.HTTP_200_OK)
def get_clients(db: Session = Depends(get_db)):
    service = ClientService(db)
    return service.get_all_clients()


@router.get("/{client_id}", response_model=ClientRead)
def get_client(client_id: int, db: Session = Depends(get_db)):
    client = ClientService(db).get_by_id(client_id)
    if client is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Клиент не найден"
        )
    return client


@router.post("/", response_model=ClientRead, status_code=status.HTTP_201_CREATED)
def create_client(client_data: ClientCreate, db: Session = Depends(get_db)):
    service = ClientService(db)

    return service.create_client(client_data)


@router.post("/{client_id}/score", status_code=status.HTTP_200_OK)
def get_score(client_id: int, db: Session = Depends(get_db)):
    score = ScoringService(db).get_score(client_id)
    if score is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Неизестный клиент"
        )
