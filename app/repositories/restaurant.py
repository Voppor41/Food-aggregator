from sqlalchemy.orm import Session

from app.models.restaurant import Restaurant

class RestaurantRepository:
    @staticmethod
    def get_all(db: Session) -> list[Restaurant]:
        return db.query(Restaurant).all()

    @staticmethod
    def get_by_id(db: Session, restaurant_id) -> Restaurant | None:
        return db.query(Restaurant).filter(Restaurant.id == restaurant_id).first()

    @staticmethod
    def create(db: Session, name: str, rating: float | None = None) -> Restaurant:
        restaurant = Restaurant(name=name, rating=rating)
        db.add(restaurant)
        db.commit()
        db.refresh(restaurant)
        return restaurant
