#!/bin/bash
source venv/bin/activate
python manage.py makemigrations
python manage.py makemigrations users
python manage.py makemigrations news
python manage.py migrate