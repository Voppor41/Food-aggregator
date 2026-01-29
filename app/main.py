from fastapi import FastAPI
from app.routers import dishes, restaurants
from app.core.database import engine, Base
from app.models import restaurant, dish

app = FastAPI(title="Food Aggregator")

app.include_router(restaurants.router)
app.include_router(dishes.router)

Base.metadata.create_all(bind=engine)