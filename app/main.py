from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from app.routers import dishes, restaurants, auth, favorites, user
from app.core.database import engine, Base
from app.models import restaurant, dish

app = FastAPI(title="Food Aggregator")

origins = [
    "http://localhost:3000",  # типичный порт React
    "http://127.0.0.1:3000",
]

app.include_router(restaurants.router)
app.include_router(dishes.router)
app.include_router(auth.router)
app.include_router(favorites.router)
app.include_router(user.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)