from fastapi import FastAPI
from app.routers import dishes

app = FastAPI(title="Food Aggregator")

app.include_router(dishes.router)