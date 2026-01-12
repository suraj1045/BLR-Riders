from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from ..db.base import Base

class LearningModule(Base):
    __tablename__ = "learning_modules"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(Text)  # Markdown content
    category = Column(String, index=True)  # e.g., "Safety", "Maintenance", "Etiquette"
    created_at = Column(DateTime, default=datetime.utcnow)
