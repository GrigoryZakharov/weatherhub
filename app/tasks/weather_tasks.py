from app.core.celery_app import celery
from app.services.weather_service import fetch_weather
from app.db.session import SessionLocal
from app.db.models.weather import Weather
from app.db.session import get_db
from sqlalchemy.orm import Session
from datetime import datetime

CITIES = ["Moscow", "London", "New York", "Tokyo"]

@celery.task
def update_weather_task(city: str):
    db: Session = next(get_db()) 
    data = fetch_weather(city) 
    weather = Weather(
        city=city,
        temperature=data["temperature"],
        description=data["description"],
        created_at=datetime.utcnow()
    )
    db.add(weather)
    db.commit()
    db.close()
    return f"{city} updated"

@celery.task
def fetch_weather_for_all():
    for city in CITIES:
        update_weather_task.delay(city)
