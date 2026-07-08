from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from .. import models, schemas

router = APIRouter(
    prefix="/order-items",
    tags=["Order Items"]
)


@router.post("/")
def create_order_item(item: schemas.OrderItemCreate, db: Session = Depends(get_db)):
    new_item = models.OrderItem(**item.model_dump())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return {"message": "Order Item Created Successfully", "order_item": new_item}


@router.get("/")
def get_order_items(db: Session = Depends(get_db)):
    return db.query(models.OrderItem).all()


@router.get("/{item_id}")
def get_order_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(models.OrderItem).filter(models.OrderItem.id == item_id).first()

    if not item:
        raise HTTPException(status_code=404, detail="Order Item Not Found")

    return item


@router.put("/{item_id}")
def update_order_item(item_id: int, item: schemas.OrderItemCreate, db: Session = Depends(get_db)):
    existing = db.query(models.OrderItem).filter(models.OrderItem.id == item_id).first()

    if not existing:
        raise HTTPException(status_code=404, detail="Order Item Not Found")

    existing.order_id = item.order_id
    existing.food_name = item.food_name
    existing.quantity = item.quantity
    existing.price = item.price

    db.commit()
    db.refresh(existing)

    return {"message": "Order Item Updated Successfully", "order_item": existing}


@router.delete("/{item_id}")
def delete_order_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(models.OrderItem).filter(models.OrderItem.id == item_id).first()

    if not item:
        raise HTTPException(status_code=404, detail="Order Item Not Found")

    db.delete(item)
    db.commit()

    return {"message": "Order Item Deleted Successfully"}