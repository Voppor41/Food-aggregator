from sqlalchemy.orm import Session
from app.models.favorite import Favorite


class FavoriteRepository:

    @staticmethod
    def add(db: Session, user_id: int, dish_id: int) -> Favorite:
        favorite = Favorite(user_id=user_id, dish_id=dish_id)
        db.add(favorite)
        db.commit()
        db.refresh(favorite)
        return favorite

    @staticmethod
    def remove(db: Session, user_id: int, dish_id: int) -> None:
        favorite = (
            db.query(Favorite)
            .filter(
                Favorite.user_id == user_id,
                Favorite.dish_id == dish_id
            )
            .first()
        )
        if favorite:
            db.delete(favorite)
            db.commit()

    @staticmethod
    def get_by_user(db: Session, user_id: int):
        return (
            db.query(Favorite)
            .filter(Favorite.user_id == user_id)
            .all()
        )
