#!/bin/sh

echo "waiting for server volume..."
until cd /app/backend
do
    echo "Waiting for server volume..."
done

echo "Waiting for db to be ready..."
python ./manage.py migrate

python ./manage.py makemigrations

python ./manage.py migrate

echo "collecting static..."
python ./manage.py collectstatic --noinput 

echo "attempt to start server..."
gunicorn backend.wsgi --bind 0.0.0.0:8000 --workers 4 --threads 4 --log-level debug --reload
# python ./manage.py runserver 0.0.0.0:8000

#####################################################################################
# Options to DEBUG Django server
# Optional commands to replace above gunicorn command

# Option 1:
# run gunicorn with debug log level
# gunicorn server.wsgi --bind 0.0.0.0:8000 --workers 1 --threads 1 --log-level debug

# Option 2:
# run development server
# DEBUG=True ./manage.py runserver 0.0.0.0:8000