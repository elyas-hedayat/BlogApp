#!/bin/sh

echo "--> Starting celery process"
celery -A blogapp.tasks worker -l info --without-gossip --without-mingle --without-heartbeat
