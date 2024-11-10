from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TestTaskWeather.settings')

app = Celery('TestTaskWeather')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    from constance import config
    from celery.schedules import crontab

    sender.add_periodic_task(
        crontab(minute=0, hour=f'*/{config.WEATHER_FETCH_INTERVAL}'),
        'news.tasks.fetch_weather_data',
        name='Fetch weather data every N hours'
    )
