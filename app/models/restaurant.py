from sqlalchemy import String, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base

class Restaurant(Base):
    __tablename__ = "restaurants"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    rating: Mapped[float] = mapped_column(Float,default=0)

    dishes: Mapped[list["Dish"]] = relationship(
        back_populates="restaurant",
        cascade="all, delete-orphan"
    )