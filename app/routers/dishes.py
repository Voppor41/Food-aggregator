from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.dish import DishCreate, DishOut, DishRead
from app.services.dish import DishService

router = APIRouter(
    prefix="/dishes",
    tags=["Dishes"],
)


@router.get("/", response_model=list[DishOut])
def get_dishes(db: Session = Depends(get_db)):
    return DishService.list_dishes(db)


@router.get(
    "/restaurant/{restaurant_id}",
    response_model=list[DishOut],
)
def get_dishes_by_restaurant(
    restaurant_id: int,
    db: Session = Depends(get_db),
):
    return DishService.list_by_restaurant(db, restaurant_id)


@router.post("/", response_model=DishRead)
def create_dish(
    dish: DishCreate,
    db: Session = Depends(get_db),
):
    return DishService.create_dish(
        db,
        name=dish.name,
        price=dish.price,
        restaurant_id=dish.restaurant_id,
    )
