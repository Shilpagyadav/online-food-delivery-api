from fastapi import FastAPI

from .database import Base, engine
from . import models

# Import all routers
from .routers import (
    users,
    restaurants,
    categories,
    food_items,
    carts,
    orders,
    order_items,
    payments,
    deliveries,
    reviews,
)

# Create all database tables
Base.metadata.create_all(bind=engine)

# Create FastAPI application
app = FastAPI(
    title="Online Food Delivery API",
    description="REST API for Online Food Delivery System",
    version="1.0.0"
)

# Register all routers
app.include_router(users.router)
app.include_router(restaurants.router)
app.include_router(categories.router)
app.include_router(food_items.router)
app.include_router(carts.router)
app.include_router(orders.router)
app.include_router(order_items.router)
app.include_router(payments.router)
app.include_router(deliveries.router)
app.include_router(reviews.router)

# Home API
@app.get("/")
def home():
    return {
        "message": "Welcome to Online Food Delivery API",
        "status": "Running Successfully"
    }