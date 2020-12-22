FROM python:3.8-buster

ENV TZ=Asia/Manila
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /app

WORKDIR /app
ADD ./app/ /app

RUN pip install --upgrade pip

RUN apt-get update \
    && apt-get install -y cron \
    && apt-get autoremove -y

RUN pip install gunicorn

RUN pip install --no-cache-dir -r requirements.txt

RUN export $(cat /app/.env | xargs)

CMD gunicorn --bind 0.0.0.0:80 app.wsgi
