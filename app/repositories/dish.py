from sqlalchemy.orm import Session

from app.models.dish import Dish

class DishRepository:
    @staticmethod
    def get_all(db: Session) -> list[Dish]:
        return db.query(Dish).all()

    @staticmethod
    def get_by_restaurant(db: Session, restaurant_id) -> list[Dish]:
        return db.query(Dish).filter(Dish.restaurant_id == restaurant_id).all()

    @staticmethod
    def create(db:Session, name: str, price: float, restaurant_id: int) -> Dish:
        dish = Dish(name=name, price=price, restaurant_id=restaurant_id)
        db.add(dish)
        db.commit()
        db.refresh(dish)
        return dish