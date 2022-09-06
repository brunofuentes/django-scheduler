
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/1'
CELERYBEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'
