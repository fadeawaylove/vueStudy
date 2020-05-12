#!/bin/sh
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
docker images | grep none | awk '{print $3}' | xargs docker rmi
