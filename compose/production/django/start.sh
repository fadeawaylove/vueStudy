#!/bin/sh
python manage.py migrate
python manage.py collectstatic --noinput
# gunicorn dog_blog.wsgi:application -w 4 -k gthread -b 0.0.0.0:8000 --chdir=/app
gunicorn -c gunicorn.py dog_blog.wsgi:application