from sqlalchemy.orm import Session

from app.repositories.user import UserRepository
from app.core.security import (
    get_password_hash,
    verify_password,
    create_access_token
)
from app.models.user import User


class AuthService:

    @staticmethod
    def register(db: Session, email: str, password: str) -> User:
        existing_user = UserRepository.get_by_email(db, email)
        if existing_user:
            raise ValueError("User already exists")

        hashed_password = get_password_hash(password)
        return UserRepository.create(
            db=db,
            email=email,
            hashed_password=hashed_password
        )

    @staticmethod
    def authenticate(db: Session, email: str, password: str) -> User:
        user = UserRepository.get_by_email(db, email)
        if not user:
            raise ValueError("Invalid credentials")

        if not verify_password(password, user.hashed_password):
            raise ValueError("Invalid credentials")

        return user

    @staticmethod
    def create_token(user: User) -> str:
        return create_access_token(
            data={"sub": str(user.id)}
        )
