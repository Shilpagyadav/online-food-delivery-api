from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from .. import models, schemas

router = APIRouter(
    prefix="/payments",
    tags=["Payments"]
)


@router.post("/")
def create_payment(payment: schemas.PaymentCreate, db: Session = Depends(get_db)):
    new_payment = models.Payment(**payment.model_dump())
    db.add(new_payment)
    db.commit()
    db.refresh(new_payment)
    return {"message": "Payment Created Successfully", "payment": new_payment}


@router.get("/")
def get_payments(db: Session = Depends(get_db)):
    return db.query(models.Payment).all()


@router.get("/{payment_id}")
def get_payment(payment_id: int, db: Session = Depends(get_db)):
    payment = db.query(models.Payment).filter(models.Payment.id == payment_id).first()

    if not payment:
        raise HTTPException(status_code=404, detail="Payment Not Found")

    return payment


@router.put("/{payment_id}")
def update_payment(payment_id: int, payment: schemas.PaymentCreate, db: Session = Depends(get_db)):
    existing = db.query(models.Payment).filter(models.Payment.id == payment_id).first()

    if not existing:
        raise HTTPException(status_code=404, detail="Payment Not Found")

    existing.order_id = payment.order_id
    existing.payment_method = payment.payment_method
    existing.payment_status = payment.payment_status
    existing.amount = payment.amount

    db.commit()
    db.refresh(existing)

    return {"message": "Payment Updated Successfully", "payment": existing}


@router.delete("/{payment_id}")
def delete_payment(payment_id: int, db: Session = Depends(get_db)):
    payment = db.query(models.Payment).filter(models.Payment.id == payment_id).first()

    if not payment:
        raise HTTPException(status_code=404, detail="Payment Not Found")

    db.delete(payment)
    db.commit()

    return {"message": "Payment Deleted Successfully"}