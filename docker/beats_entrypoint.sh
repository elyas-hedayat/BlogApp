#!/bin/sh

echo "--> Starting beats process"
celery -A blogapp.tasks beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler

