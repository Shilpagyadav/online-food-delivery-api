from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from .. import models, schemas

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

# -----------------------------
# CREATE USER
# -----------------------------
@router.post("/")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    new_user = models.User(
        name=user.name,
        email=user.email,
        phone=user.phone,
        password=user.password,
        address=user.address
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User Created Successfully",
        "user_id": new_user.id
    }


# -----------------------------
# GET ALL USERS
# -----------------------------
@router.get("/")
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users


# -----------------------------
# GET USER BY ID
# -----------------------------
@router.get("/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User Not Found"
        )

    return user


# -----------------------------
# UPDATE USER
# -----------------------------
@router.put("/{user_id}")
def update_user(user_id: int, user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(models.User).filter(models.User.id == user_id).first()

    if not existing_user:
        raise HTTPException(
            status_code=404,
            detail="User Not Found"
        )

    existing_user.name = user.name
    existing_user.email = user.email
    existing_user.phone = user.phone
    existing_user.password = user.password
    existing_user.address = user.address

    db.commit()
    db.refresh(existing_user)

    return {
        "message": "User Updated Successfully",
        "user": existing_user
    }


# -----------------------------
# DELETE USER
# -----------------------------
@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User Not Found"
        )

    db.delete(user)
    db.commit()

    return {
        "message": "User Deleted Successfully"
    }