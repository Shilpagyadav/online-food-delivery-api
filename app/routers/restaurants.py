from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from .. import models, schemas

router = APIRouter(
    prefix="/restaurants",
    tags=["Restaurants"]
)

# Create Restaurant
@router.post("/")
def create_restaurant(
    restaurant: schemas.RestaurantCreate,
    db: Session = Depends(get_db)
):
    new_restaurant = models.Restaurant(
        name=restaurant.name,
        owner=restaurant.owner,
        email=restaurant.email,
        phone=restaurant.phone,
        address=restaurant.address
    )

    db.add(new_restaurant)
    db.commit()
    db.refresh(new_restaurant)

    return {
        "message": "Restaurant Created Successfully",
        "restaurant_id": new_restaurant.id
    }


# Get All Restaurants
@router.get("/")
def get_restaurants(db: Session = Depends(get_db)):
    return db.query(models.Restaurant).all()


# Get Restaurant By ID
@router.get("/{restaurant_id}")
def get_restaurant(restaurant_id: int, db: Session = Depends(get_db)):
    restaurant = db.query(models.Restaurant).filter(
        models.Restaurant.id == restaurant_id
    ).first()

    if not restaurant:
        raise HTTPException(status_code=404, detail="Restaurant Not Found")

    return restaurant


# Update Restaurant
@router.put("/{restaurant_id}")
def update_restaurant(
    restaurant_id: int,
    restaurant: schemas.RestaurantCreate,
    db: Session = Depends(get_db)
):
    existing = db.query(models.Restaurant).filter(
        models.Restaurant.id == restaurant_id
    ).first()

    if not existing:
        raise HTTPException(status_code=404, detail="Restaurant Not Found")

    existing.name = restaurant.name
    existing.owner = restaurant.owner
    existing.email = restaurant.email
    existing.phone = restaurant.phone
    existing.address = restaurant.address

    db.commit()
    db.refresh(existing)

    return {
        "message": "Restaurant Updated Successfully"
    }


# Delete Restaurant
@router.delete("/{restaurant_id}")
def delete_restaurant(restaurant_id: int, db: Session = Depends(get_db)):
    restaurant = db.query(models.Restaurant).filter(
        models.Restaurant.id == restaurant_id
    ).first()

    if not restaurant:
        raise HTTPException(status_code=404, detail="Restaurant Not Found")

    db.delete(restaurant)
    db.commit()

    return {
        "message": "Restaurant Deleted Successfully"
    }