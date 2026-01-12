from datetime import datetime
from sqlalchemy import Boolean, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from ..db.base import Base

class User(Base):
    """User model for storing user accounts"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    full_name = Column(String(100))
    phone_number = Column(String(20))
    is_active = Column(Boolean(), default=True)
    is_verified = Column(Boolean(), default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    rides = relationship("Ride", back_populates="organizer")
    # ride_participations = relationship("RideParticipant", back_populates="user")

    def __repr__(self):
        return f"<User {self.email}>"