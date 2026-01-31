from fastapi import FastAPI
from app.routers import dishes, restaurants, auth, favorites, user
from app.core.database import engine, Base
from app.models import restaurant, dish

app = FastAPI(title="Food Aggregator")

app.include_router(restaurants.router)
app.include_router(dishes.router)
app.include_router(auth.router)
app.include_router(favorites.router)
app.include_router(user.router)

Base.metadata.create_all(bind=engine)