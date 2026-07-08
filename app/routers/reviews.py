from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from .. import models, schemas

router = APIRouter(
    prefix="/reviews",
    tags=["Reviews"]
)


@router.post("/")
def create_review(review: schemas.ReviewCreate, db: Session = Depends(get_db)):
    new_review = models.Review(**review.model_dump())
    db.add(new_review)
    db.commit()
    db.refresh(new_review)
    return {"message": "Review Added Successfully", "review": new_review}


@router.get("/")
def get_reviews(db: Session = Depends(get_db)):
    return db.query(models.Review).all()


@router.get("/{review_id}")
def get_review(review_id: int, db: Session = Depends(get_db)):
    review = db.query(models.Review).filter(models.Review.id == review_id).first()

    if not review:
        raise HTTPException(status_code=404, detail="Review Not Found")

    return review


@router.put("/{review_id}")
def update_review(review_id: int, review: schemas.ReviewCreate, db: Session = Depends(get_db)):
    existing = db.query(models.Review).filter(models.Review.id == review_id).first()

    if not existing:
        raise HTTPException(status_code=404, detail="Review Not Found")

    existing.user_name = review.user_name
    existing.restaurant_name = review.restaurant_name
    existing.rating = review.rating
    existing.review = review.review

    db.commit()
    db.refresh(existing)

    return {"message": "Review Updated Successfully", "review": existing}


@router.delete("/{review_id}")
def delete_review(review_id: int, db: Session = Depends(get_db)):
    review = db.query(models.Review).filter(models.Review.id == review_id).first()

    if not review:
        raise HTTPException(status_code=404, detail="Review Not Found")

    db.delete(review)
    db.commit()

    return {"message": "Review Deleted Successfully"}