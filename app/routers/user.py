from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.user import UserCreate, UserRead
from app.services.user import UserService

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=UserRead)
def create_user(data: UserCreate, db: Session = Depends(get_db)):
    return UserService.create(db, data)
