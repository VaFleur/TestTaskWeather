from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TestTaskWeather.settings')
app = Celery('TestTaskWeather')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'fetch-weather-every-hour': {
        'task': 'news.tasks.fetch_weather_data',
        'schedule': crontab(minute=0, hour='*/1'),
    },
}
