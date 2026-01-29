from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.favorite import Favorite


class FavoriteService:

    @staticmethod
    def add(db: Session, user_id: int, dish_id: int) -> Favorite:
        exists = db.query(Favorite).filter_by(
            user_id=user_id,
            dish_id=dish_id
        ).first()

        if exists:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Dish already in favorites"
            )

        fav = Favorite(user_id=user_id, dish_id=dish_id)
        db.add(fav)
        db.commit()
        db.refresh(fav)
        return fav

    @staticmethod
    def list(db: Session, user_id: int):
        return db.query(Favorite).filter_by(user_id=user_id).all()

    @staticmethod
    def remove(db: Session, user_id: int, dish_id: int):
        fav = db.query(Favorite).filter_by(
            user_id=user_id,
            dish_id=dish_id
        ).first()

        if not fav:
            raise HTTPException(status_code=404, detail="Not found")

        db.delete(fav)
        db.commit()
