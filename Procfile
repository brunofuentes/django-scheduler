web: python manage.py runserver 0.0.0.0:$PORT
release: python manage.py migrate
worker: celery -A scheduler worker --loglevel=info -P threads
