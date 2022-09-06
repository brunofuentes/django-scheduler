from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scheduler.settings')
app = Celery('scheduler', broker='redis://localhost:6379/0')
app.conf.enable_utc = False
app.conf.timezone = 'Europe/Berlin'
app.conf.update(timezone = 'Europe/Berlin')
app.config_from_object(settings, namespace='CELERY')

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')