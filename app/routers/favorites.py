from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.favorite import FavoriteCreate, FavoriteRead
from app.services.favorite import FavoriteService

router = APIRouter(prefix="/favorites", tags=["Favorites"])


@router.post("/", response_model=FavoriteRead)
def add_favorite(
    data: FavoriteCreate,
    db: Session = Depends(get_db),
    user_id: int = 1  # временно, потом заменим на auth
):
    return FavoriteService.add(db, user_id, data.dish_id)


@router.get("/", response_model=list[FavoriteRead])
def list_favorites(
    db: Session = Depends(get_db),
    user_id: int = 1
):
    return FavoriteService.list(db, user_id)


@router.delete("/{dish_id}", status_code=204)
def remove_favorite(
    dish_id: int,
    db: Session = Depends(get_db),
    user_id: int = 1
):
    FavoriteService.remove(db, user_id, dish_id)
