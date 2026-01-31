from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.restaurant import RestaurantOut, RestaurantCreate
from app.services.restaurant import RestaurantService

router = APIRouter(prefix="/restaurants", tags=["Restaurants"])

@router.get("/", response_model=list[RestaurantOut])
def get_restaurant(db: Session = Depends(get_db)):
    return RestaurantService.list_restaurant(db)

@router.post("/", response_model=RestaurantOut)
def create_restaurant(data: RestaurantCreate, db: Session = Depends(get_db)):
    return RestaurantService.create_restaurant(db, name=data.name, rating=data.rating)