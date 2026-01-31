from sqlalchemy.orm import Session
from app.repositories.favorite import FavoriteRepository


class FavoriteService:

    @staticmethod
    def add(db: Session, user_id: int, dish_id: int):
        return FavoriteRepository.add(db, user_id, dish_id)

    @staticmethod
    def remove(db: Session, user_id: int, dish_id: int):
        FavoriteRepository.remove(db, user_id, dish_id)

    @staticmethod
    def list(db: Session, user_id: int):
        return FavoriteRepository.get_by_user(db, user_id)
