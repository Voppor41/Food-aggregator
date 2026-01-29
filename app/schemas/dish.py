from pydantic import BaseModel


class DishBase(BaseModel):
    name: str
    price: float


class DishCreate(DishBase):
    restaurant_id: int


class DishOut(DishBase):
    id: int
    restaurant_id: int

    class Config:
        from_attributes = True
