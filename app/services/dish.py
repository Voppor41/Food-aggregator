from sqlalchemy.orm import Session

from app.models.dish import Dish
from app.repositories.dish import DishRepository


class DishService:
    @staticmethod
    def list_dishes(db: Session) -> list[Dish]:
        return DishRepository.get_all(db)

    @staticmethod
    def list_by_restaurant(
        db: Session,
        restaurant_id: int,
    ) -> list[Dish]:
        return DishRepository.get_by_restaurant(db, restaurant_id)

    @staticmethod
    def create_dish(
        db: Session,
        *,
        name: str,
        price: float,
        restaurant_id: int,
    ) -> Dish:
        return DishRepository.create(
            db,
            name=name,
            price=price,
            restaurant_id=restaurant_id,
        )
