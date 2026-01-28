from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.dish import Dish
from app.schemas.dish import DishCreate, DishRead

router = APIRouter(
    prefix="/dishes",
    tags=["Dishes"]
)


@router.post("/", response_model=DishRead)
def create_dish(
    dish_in: DishCreate,
    db: Session = Depends(get_db)
):
    dish = Dish(**dish_in.model_dump())
    db.add(dish)
    db.commit()
    db.refresh(dish)
    return dish


@router.get("/", response_model=list[DishRead])
def get_dishes(db: Session = Depends(get_db)):
    return db.query(Dish).all()


@router.get("/{dish_id}", response_model=DishRead)
def get_dish(
    dish_id: int,
    db: Session = Depends(get_db)
):
    dish = db.query(Dish).get(dish_id)
    if not dish:
        raise HTTPException(status_code=404, detail="Dish not found")
    return dish
