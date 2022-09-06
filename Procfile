web: python manage.py runserver 0.0.0.0:$PORT
release: python manage.py migrate
celery -A scheduler worker --loglevel=info -P threads
