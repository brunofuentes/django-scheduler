# Task Scheduler App

APP URL: [https://django-task-scheduler.herokuapp.com/admin/](https://django-task-scheduler.herokuapp.com/admin/)

## Instructions

1. with the given credentials, log in to the admin panel and open Requests
2. Add your HTTP Request with a name, choose GET or POST, add your URL, add a start date and time and save it.
3. You will see your inputs in the requests table. You can modify if only before the request has been made.
4. The requests table will be updated once the request has been made with the following infos: STATUS, STATUS_CODE and RES_BODY (3 right columns)
5. Additional infos of the requests can be found at Task Results tab, such as id, task name, complete datetime, state and worker.

## Tech Stack:

-   [Python 3.7.13](https://www.python.org/downloads/release/python-3713/)
-   [Django 3.2.15](https://docs.djangoproject.com/en/3.2/)
-   [Celery 5.1.2](https://docs.celeryq.dev/en/stable/)
-   [PostgreSQL](https://www.postgresql.org/)
-   [Redis](https://redis.io/)

List of all dependencies: [requirements.txt](https://github.com/brunofuentes/django-scheduler/blob/main/requirements.txt)

## Running the project locally:

Make sure you have Redis installed. Follow [this tutorial](https://redis.io/docs/getting-started/installation/install-redis-on-windows/) to get it done.

1. Clone this repository
2. Initiate and activate a virtualenv:

```
python3 install virtualenv
python -m virtualenv env
```

3. Install all dependencies:

```
pip install requirements.txt
```

4. Run Django Project / Migrations:

```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

5. In order to fully run the application you need to have 3 terminals running:

-   django server running
-   celery worker
-   redis server

## Usefull commands:

-   To start a celery worker:

```
celery -A scheduler worker --loglevel=info -P threads (for windows)
celery -A scheduler worker --loglevel=info (for UNIX Systems)

```

-   To start redis (on a windows, WSL Terminal):

```
redis-server
```
