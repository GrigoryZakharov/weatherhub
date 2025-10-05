from fastapi import FastAPI, APIRouter, Depends
from app.api.routes_weather import router as weather_router
from sqlalchemy.orm import Session
from app.db.models.weather import Weather
from app.db.session import get_db

from fastapi import FastAPI
from app.api.routes_weather import router as weather_router

app = FastAPI(title="WeatherHub API")

app.include_router(weather_router, prefix="/weather")

@app.get("/")
def root():
    return {"status": "ok", "message": "WeatherHub API running"}

    