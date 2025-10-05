from celery.schedules import crontab
from app.core.celery_app import celery
from app.tasks.weather_tasks import update_weather_task

CITIES = ["Moscow", "London", "New York", "Tokyo"]

@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(crontab(minute="*"), fetch_weather_for_all.s())

@celery.task
def fetch_weather_for_all():
    for city in CITIES:
        update_weather_task.delay(city)
