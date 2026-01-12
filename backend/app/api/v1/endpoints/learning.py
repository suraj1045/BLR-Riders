from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ....db.base import get_db
from ....models.learning import LearningModule
from ....models.user import User
from ....schemas import learning as learning_schemas
from app.services.auth import get_current_active_user

router = APIRouter()

@router.post("/", response_model=learning_schemas.LearningModule)
def create_learning_module(
    module: learning_schemas.LearningModuleCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    # In a real app, check for admin privileges here
    db_module = LearningModule(**module.dict())
    db.add(db_module)
    db.commit()
    db.refresh(db_module)
    return db_module

@router.get("/", response_model=List[learning_schemas.LearningModule])
def read_learning_modules(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    modules = db.query(LearningModule).offset(skip).limit(limit).all()
    return modules
