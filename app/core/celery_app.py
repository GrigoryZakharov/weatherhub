from celery import Celery
import os

REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379/0")

celery = Celery(
    "weatherhub",
    broker=REDIS_URL,
    backend=REDIS_URL,
    include=["app.tasks.weather_tasks"],
)


celery.conf.task_routes = {
    "app.tasks.weather_tasks.update_weather_task": {"queue": "celery"}
}

celery.conf.beat_schedule = {
    'update-all-cities-every-10-minutes': {
        'task': 'app.tasks.weather_tasks.fetch_weather_for_all',
        'schedule': 600,
    },
}
