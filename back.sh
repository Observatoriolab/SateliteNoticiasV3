#!/bin/bash
python manage.py makemigrations
python manage.py makemigrations users
python manage.py makemigrations news
python manage.py migrate