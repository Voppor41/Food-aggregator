from pydantic import BaseModel


class DishBase(BaseModel):
    name: str
    price: int


class DishCreate(DishBase):
    restaurant_id: int


class DishRead(DishBase):
    id: int
    restaurant_id: int

    model_config = {"from_attributes": True}
