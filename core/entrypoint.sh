#!/bin/env sh

python manage.py migrate
python manage.py collectstatic --no-input
gunicorn --bind 0.0.0.0:8000 core.wsgi

exec "$@"