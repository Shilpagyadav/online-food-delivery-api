from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from .. import models, schemas

router = APIRouter(
    prefix="/deliveries",
    tags=["Deliveries"]
)


@router.post("/")
def create_delivery(delivery: schemas.DeliveryCreate, db: Session = Depends(get_db)):
    new_delivery = models.Delivery(**delivery.model_dump())
    db.add(new_delivery)
    db.commit()
    db.refresh(new_delivery)
    return {"message": "Delivery Created Successfully", "delivery": new_delivery}


@router.get("/")
def get_deliveries(db: Session = Depends(get_db)):
    return db.query(models.Delivery).all()


@router.get("/{delivery_id}")
def get_delivery(delivery_id: int, db: Session = Depends(get_db)):
    delivery = db.query(models.Delivery).filter(models.Delivery.id == delivery_id).first()

    if not delivery:
        raise HTTPException(status_code=404, detail="Delivery Not Found")

    return delivery


@router.put("/{delivery_id}")
def update_delivery(delivery_id: int, delivery: schemas.DeliveryCreate, db: Session = Depends(get_db)):
    existing = db.query(models.Delivery).filter(models.Delivery.id == delivery_id).first()

    if not existing:
        raise HTTPException(status_code=404, detail="Delivery Not Found")

    existing.order_id = delivery.order_id
    existing.delivery_person = delivery.delivery_person
    existing.delivery_status = delivery.delivery_status
    existing.delivery_address = delivery.delivery_address

    db.commit()
    db.refresh(existing)

    return {"message": "Delivery Updated Successfully", "delivery": existing}


@router.delete("/{delivery_id}")
def delete_delivery(delivery_id: int, db: Session = Depends(get_db)):
    delivery = db.query(models.Delivery).filter(models.Delivery.id == delivery_id).first()

    if not delivery:
        raise HTTPException(status_code=404, detail="Delivery Not Found")

    db.delete(delivery)
    db.commit()

    return {"message": "Delivery Deleted Successfully"}