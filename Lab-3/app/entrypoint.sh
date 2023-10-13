#!/bin/sh

<<<<<<< HEAD
python manage.py migrate --no-input

python manage.py collectstatic --no-input

DJANGO_SUPERUSER_PASSWORD=$SUPER_USER_PASSWORD python manage.py createsuperuser --username $SUPER_USER_NAME --email $SUPER_USER_EMAIL --no-input
=======
#python manage.py migrate --no-input
#python manage.py collectstatic --no-input

#DJANGO_SUPERUSER_PASSWORD=$SUPER_USER_PASSWORD python manage.py createsuperuser --username $SUPER_USER_NAME --email $SUPER_USER_EMAIL --noinput
>>>>>>> 73a4617a0c1914837a1dbb876ffd35313b238f4a

#gunicorn django_project.wsgi:application --bind 0.0.0.0:8000
python manage.py runserver 0.0.0.0:8000