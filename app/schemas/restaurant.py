from pydantic import BaseModel


class RestaurantBase(BaseModel):
    name: str
    rating: float | None = None


class RestaurantCreate(RestaurantBase):
    pass


class RestaurantOut(RestaurantBase):
    id: int

    class Config:
        from_attributes = True
