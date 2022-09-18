#!/bin/bash

echo >&2 'Migrating to Database'
python manage.py migrate --no-input

echo >&2 'collecting static files'
python manage.py collectstatic --no-input

echo >&2 'starting server'
python manage.py runserver 0.0.0.0:$PORT
# /usr/local/bin/gunicorn config.wsgi:application -w 2 -b :$PORT --reload
