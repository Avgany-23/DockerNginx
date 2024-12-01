#!/bin/bash

python manage.py migrate
gunicorn drf.wsgi -b 0.0.0.0:8000
