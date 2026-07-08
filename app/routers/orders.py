from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from .. import models, schemas

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


@router.post("/")
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    new_order = models.Order(**order.model_dump())
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return {"message": "Order Created Successfully", "order": new_order}


@router.get("/")
def get_orders(db: Session = Depends(get_db)):
    return db.query(models.Order).all()


@router.get("/{order_id}")
def get_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(models.Order).filter(models.Order.id == order_id).first()

    if not order:
        raise HTTPException(status_code=404, detail="Order Not Found")

    return order


@router.put("/{order_id}")
def update_order(order_id: int, order: schemas.OrderCreate, db: Session = Depends(get_db)):
    existing = db.query(models.Order).filter(models.Order.id == order_id).first()

    if not existing:
        raise HTTPException(status_code=404, detail="Order Not Found")

    existing.user_name = order.user_name
    existing.order_date = order.order_date
    existing.total_amount = order.total_amount
    existing.status = order.status

    db.commit()
    db.refresh(existing)

    return {"message": "Order Updated Successfully", "order": existing}


@router.delete("/{order_id}")
def delete_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(models.Order).filter(models.Order.id == order_id).first()

    if not order:
        raise HTTPException(status_code=404, detail="Order Not Found")

    db.delete(order)
    db.commit()

    return {"message": "Order Deleted Successfully"}