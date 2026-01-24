from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.dish import Dish
from app.schemas.dish import DishOut

router = APIRouter(prefix="/dishes", tags=["Dishes"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[DishOut])
def get_dish(db: SessionLocal = Depends(get_db)):
    return db.query(Dish).all()