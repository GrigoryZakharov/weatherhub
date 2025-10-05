from fastapi import FastAPI, Depends, APIRouter, HTTPException, status
from app.db.session import get_db
from sqlalchemy.orm import Session
from app.db.models.weather import Weather
from typing import List
from app.tasks.scheduler import CITIES
from app.schemas.weather import WeatherResponse, WeatherListResponse, TaskResponse, WeatherCreate
from datetime import datetime
from app.tasks.weather_tasks import update_weather_task
from typing import List

router = APIRouter(
    tags=["Weather"]
)

@router.get("/", response_model = WeatherResponse)
def get_weather(city: str, db: Session = Depends(get_db)):
    record = (
        db.query(Weather)
        .filter(Weather.city == city)
        .order_by(Weather.created_at.desc())
        .first()
    )
    if not record:
        raise HTTPException(status_code=404, detail="City not found")
    
    return WeatherResponse(
        city = record.city,
        temperature = record.temperature,
        description = record.description,
        created_at = record.created_at,
    )
    
@router.get("/all", response_model = List[WeatherResponse])
def get_all(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    records = db.query(Weather).order_by(Weather.created_at.desc()).offset(skip).limit(limit).all()
    return [
        WeatherResponse(
            city = r.city,
            temperature = r.temperature,
            description = r.description,
            created_at = r.created_at,
        )
        for r in records
    ]

@router.get("/cities", response_model = List[str])
def get_cities():
    return CITIES
