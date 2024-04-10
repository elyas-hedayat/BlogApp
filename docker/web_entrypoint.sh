#!/bin/sh

# Apply database migrations
echo "Apply database migrations"
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput

echo "Load initial data"
python manage.py loaddata initial_data.json

if [ "$DJANGO_SUPERUSER_EMAIL" ]
then
    python manage.py createsuperuser \
        --noinput \
        --email $DJANGO_SUPERUSER_EMAIL
fi

# Start server
echo "--> Starting web process"
gunicorn config.wsgi:application -b 0.0.0.0:8000