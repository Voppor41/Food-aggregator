from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from app.db.base import Base


class Favorite(Base):
    __tablename__ = "favorites"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    dish_id = Column(Integer, ForeignKey("dishes.id", ondelete="CASCADE"))

    user = relationship("User", back_populates="favorites")
    dish = relationship("Dish")

    __table_args__ = (
        UniqueConstraint("user_id", "dish_id", name="uq_user_dish"),
    )
