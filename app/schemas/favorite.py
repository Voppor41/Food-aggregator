from pydantic import BaseModel


class FavoriteCreate(BaseModel):
    dish_id: int


class FavoriteRead(BaseModel):
    id: int
    dish_id: int

    class Config:
        from_attributes = True
