from pydantic import BaseModel

class DishOut(BaseModel):
    id: int
    name: str
    price: int
    restaurant_id: int

    class Config:
        from_attributes = True