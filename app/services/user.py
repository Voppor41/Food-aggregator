from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import get_password_hash


class UserService:

    @staticmethod
    def create(db: Session, data: UserCreate) -> User:
        user = User(
            email=data.email,
            hashed_password=get_password_hash(data.password)
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
