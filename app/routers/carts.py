from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from .. import models, schemas

router = APIRouter(
    prefix="/cart",
    tags=["Cart"]
)

# Create Cart
@router.post("/")
def create_cart(cart: schemas.CartCreate, db: Session = Depends(get_db)):
    new_cart = models.Cart(**cart.model_dump())

    db.add(new_cart)
    db.commit()
    db.refresh(new_cart)

    return {
        "message": "Cart Created Successfully",
        "cart": new_cart
    }


# Get All Cart Items
@router.get("/")
def get_cart(db: Session = Depends(get_db)):
    return db.query(models.Cart).all()


# Get Cart By ID
@router.get("/{cart_id}")
def get_cart_item(cart_id: int, db: Session = Depends(get_db)):
    cart = db.query(models.Cart).filter(models.Cart.id == cart_id).first()

    if not cart:
        raise HTTPException(status_code=404, detail="Cart Item Not Found")

    return cart


# Update Cart
@router.put("/{cart_id}")
def update_cart(cart_id: int, cart: schemas.CartCreate, db: Session = Depends(get_db)):
    existing_cart = db.query(models.Cart).filter(models.Cart.id == cart_id).first()

    if not existing_cart:
        raise HTTPException(status_code=404, detail="Cart Item Not Found")

    existing_cart.user_name = cart.user_name
    existing_cart.food_name = cart.food_name
    existing_cart.quantity = cart.quantity
    existing_cart.total_price = cart.total_price

    db.commit()
    db.refresh(existing_cart)

    return {
        "message": "Cart Updated Successfully",
        "cart": existing_cart
    }


# Delete Cart
@router.delete("/{cart_id}")
def delete_cart(cart_id: int, db: Session = Depends(get_db)):
    cart = db.query(models.Cart).filter(models.Cart.id == cart_id).first()

    if not cart:
        raise HTTPException(status_code=404, detail="Cart Item Not Found")

    db.delete(cart)
    db.commit()

    return {
        "message": "Cart Deleted Successfully"
    }