from pydantic import BaseModel
from app.schemas.dish import DishRead


class RestaurantBase(BaseModel):
    name: str


class RestaurantCreate(RestaurantBase):
    pass


class RestaurantRead(RestaurantBase):
    id: int
    dishes: list[DishRead] = []

    model_config = {"from_attributes": True}
