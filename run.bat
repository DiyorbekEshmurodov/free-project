@echo off
start /b ngrok http 8000
python manage.py runserver 8000