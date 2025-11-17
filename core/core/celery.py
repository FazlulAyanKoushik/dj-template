import os
from celery import Celery
from decouple import config

TIME_ZONE = config("TIME_ZONE")

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

app.conf.update(
    broker_url="redis://dj_redis:6379",  # Broker URL for Redis
    result_backend="redis://dj_redis:6379",  # Result backend for Redis
    task_serializer="json",  # Task serialization format
    accept_content=["json"],  # Accept only JSON content for tasks
    result_serializer="json",  # Result serialization format
    timezone=TIME_ZONE,  # Set the timezone for Celery tasks
)


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

