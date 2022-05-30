import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Bday.settings')

app = Celery('Bday')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'every-30-seconds': {
        'task': 'wisher.tasks.wish',
        'schedule': crontab()
    },
}
app.conf.timezone = 'Asia/kolkata'

app.autodiscover_tasks()
