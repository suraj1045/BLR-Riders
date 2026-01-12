from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

# Base Schema
class RideBase(BaseModel):
    title: str
    description: Optional[str] = None
    date: datetime
    route: str
    difficulty: str

# Schema for creating a ride
class RideCreate(RideBase):
    pass

# Schema for reading a ride (includes ID and organizer)
class Ride(RideBase):
    id: int
    organizer_id: int
    created_at: datetime

    class Config:
        orm_mode = True
