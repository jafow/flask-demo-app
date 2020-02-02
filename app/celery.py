""" worker"""
import os

from celery import Celery
from app.config import celery_config

config = celery_config(os.getenv("FLASK_ENV"))

queue = Celery("taskq", backend=config.CELERY_RESULT_BACKEND, broker=config.CELERY_BROKER_URL)


if __name__ == "__main__":
    queue.start()
