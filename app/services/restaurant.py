from sqlalchemy.orm import Session

from app.repositories.restaurant import RestaurantRepository
from app.models.restaurant import Restaurant

class RestaurantService:
    @staticmethod
    def list_restaurant(db: Session) -> list[Restaurant]:
        return RestaurantRepository.get_all(db)

    @staticmethod
    def create_restaurant(db: Session, name: str, rating: float | None = None) -> Restaurant:
        return RestaurantRepository.create(db, name, rating)

