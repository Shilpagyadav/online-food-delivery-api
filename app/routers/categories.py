from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from .. import models, schemas

router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)

@router.post("/")
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    new_category = models.Category(
        name=category.name,
        description=category.description
    )

    db.add(new_category)
    db.commit()
    db.refresh(new_category)

    return {
        "message": "Category Created Successfully",
        "category_id": new_category.id
    }


@router.get("/")
def get_categories(db: Session = Depends(get_db)):
    return db.query(models.Category).all()


@router.get("/{category_id}")
def get_category(category_id: int, db: Session = Depends(get_db)):
    category = db.query(models.Category).filter(
        models.Category.id == category_id
    ).first()

    if not category:
        raise HTTPException(status_code=404, detail="Category Not Found")

    return category


@router.put("/{category_id}")
def update_category(category_id: int, category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    existing = db.query(models.Category).filter(
        models.Category.id == category_id
    ).first()

    if not existing:
        raise HTTPException(status_code=404, detail="Category Not Found")

    existing.name = category.name
    existing.description = category.description

    db.commit()
    db.refresh(existing)

    return {"message": "Category Updated Successfully"}


@router.delete("/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_db)):
    category = db.query(models.Category).filter(
        models.Category.id == category_id
    ).first()

    if not category:
        raise HTTPException(status_code=404, detail="Category Not Found")

    db.delete(category)
    db.commit()

    return {"message": "Category Deleted Successfully"}