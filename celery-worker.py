from app.core.celery_app import celery

from app.tasks import weather_tasks

if __name__ == "__main__":
    celery.start()
