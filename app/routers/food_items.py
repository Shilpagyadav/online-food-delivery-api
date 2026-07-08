from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from .. import models, schemas

router = APIRouter(
    prefix="/food-items",
    tags=["Food Items"]
)

@router.post("/")
def create_food_item(food: schemas.FoodItemCreate, db: Session = Depends(get_db)):
    new_food = models.FoodItem(
        name=food.name,
        description=food.description,
        price=food.price,
        restaurant=food.restaurant,
        category=food.category
    )

    db.add(new_food)
    db.commit()
    db.refresh(new_food)

    return {
        "message": "Food Item Created Successfully",
        "food_item_id": new_food.id
    }


@router.get("/")
def get_food_items(db: Session = Depends(get_db)):
    return db.query(models.FoodItem).all()


@router.get("/{food_id}")
def get_food_item(food_id: int, db: Session = Depends(get_db)):
    food = db.query(models.FoodItem).filter(models.FoodItem.id == food_id).first()

    if not food:
        raise HTTPException(status_code=404, detail="Food Item Not Found")

    return food


@router.put("/{food_id}")
def update_food_item(food_id: int, food: schemas.FoodItemCreate, db: Session = Depends(get_db)):
    existing = db.query(models.FoodItem).filter(models.FoodItem.id == food_id).first()

    if not existing:
        raise HTTPException(status_code=404, detail="Food Item Not Found")

    existing.name = food.name
    existing.description = food.description
    existing.price = food.price
    existing.restaurant = food.restaurant
    existing.category = food.category

    db.commit()
    db.refresh(existing)

    return {"message": "Food Item Updated Successfully"}


@router.delete("/{food_id}")
def delete_food_item(food_id: int, db: Session = Depends(get_db)):
    food = db.query(models.FoodItem).filter(models.FoodItem.id == food_id).first()

    if not food:
        raise HTTPException(status_code=404, detail="Food Item Not Found")

    db.delete(food)
    db.commit()

    return {"message": "Food Item Deleted Successfully"}