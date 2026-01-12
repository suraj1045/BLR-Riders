from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from ....db.base import get_db
from ....models.ride import Ride
from ....models.user import User
from ....schemas import ride as ride_schemas
from app.services.auth import get_current_active_user

router = APIRouter()

@router.post("/", response_model=ride_schemas.Ride)
def create_ride(
    ride: ride_schemas.RideCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    db_ride = Ride(**ride.dict(), organizer_id=current_user.id)
    db.add(db_ride)
    db.commit()
    db.refresh(db_ride)
    return db_ride

@router.get("/", response_model=List[ride_schemas.Ride])
def read_rides(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    rides = db.query(Ride).offset(skip).limit(limit).all()
    return rides

@router.get("/{ride_id}", response_model=ride_schemas.Ride)
def read_ride(
    ride_id: int,
    db: Session = Depends(get_db)
):
    ride = db.query(Ride).filter(Ride.id == ride_id).first()
    if ride is None:
        raise HTTPException(status_code=404, detail="Ride not found")
    return ride
