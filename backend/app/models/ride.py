from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from ..db.base import Base

class Ride(Base):
    __tablename__ = "rides"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    date = Column(DateTime)
    route = Column(String)  # Could be a JSON string or simple text for now
    difficulty = Column(String)  # e.g., "Beginner", "Intermediate", "Expert"
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Foreign Keys
    organizer_id = Column(Integer, ForeignKey("users.id"))
    
    # Relationships
    organizer = relationship("User", back_populates="rides")
