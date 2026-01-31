from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.deps import get_current_user
from app.services.favorite import FavoriteService
from app.schemas.favorite import FavoriteCreate

router = APIRouter(
    prefix="/favorites",
    tags=["Favorites"]
)


@router.post("", status_code=status.HTTP_201_CREATED)
def add_favorite(
    data: FavoriteCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    return FavoriteService.add(db, user.id, data.dish_id)


@router.delete("/{dish_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_favorite(
    dish_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    FavoriteService.remove(db, user.id, dish_id)


@router.get("")
def list_favorites(
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    return FavoriteService.list(db, user.id)
