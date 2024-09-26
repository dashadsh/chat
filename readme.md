daphne -p 8000 mywebsite.asgi:application \
uvicorn mywebsite.asgi:application --host 127.0.0.1 --port 8000 \


if daphne added to installed apps:\
python3 manage.py runserver 


