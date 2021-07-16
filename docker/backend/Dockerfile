# docker/backend/Dockerfile
FROM python:3.9.0-alpine

RUN mkdir -p /app
RUN mkdir -p /app/backend
RUN mkdir -p /app/docker

WORKDIR /app

RUN apk update
RUN apk add bash && apk --no-cache add dos2unix
RUN apk --no-cache add mariadb-client
RUN apk add --no-cache mariadb-dev build-base jpeg-dev
RUN pip install --upgrade pip
RUN pip install gunicorn
RUN pip install mysqlclient

ADD ./backend/requirements.txt /app/backend/
RUN pip install --no-cache -r /app/backend/requirements.txt


ADD ./docker /app/docker
ADD ./backend /app/backend

COPY ./docker/backend/wsgi-entrypoint.sh /app/docker/backend/wsgi-entrypoint.sh

RUN chmod +x /app/docker/backend/wsgi-entrypoint.sh

RUN dos2unix /app/docker/backend/wsgi-entrypoint.sh && apk del dos2unix

RUN echo "running"
