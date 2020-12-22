FROM python:3.8-alpine

ENV TZ=Asia/Manila
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /app

WORKDIR /app
ADD ./app/ /app

RUN pip install --upgrade pip

RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev
RUN apk add --no-cache jpeg-dev zlib-dev
RUN apk add --no-cache --virtual .build-deps build-base linux-headers

RUN pip install --no-cache-dir -r requirements.txt

CMD python /app/manage.py runserver 0.0.0.0:80
