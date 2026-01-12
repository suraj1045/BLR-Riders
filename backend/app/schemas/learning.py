from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class LearningModuleBase(BaseModel):
    title: str
    content: str
    category: str

class LearningModuleCreate(LearningModuleBase):
    pass

class LearningModule(LearningModuleBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
