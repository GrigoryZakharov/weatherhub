from pydantic import BaseModel
from datetime import datetime
from typing import List

class WeatherResponse(BaseModel):
    city: str
    temperature: float
    description: str
    created_at: datetime

class WeatherListResponse(BaseModel):
    items: List[WeatherResponse]
    total: int

class WeatherCreate(BaseModel):
    city: str
    temperature: float
    description: str

class TaskResponse(BaseModel):
  status: str
  task_id: str