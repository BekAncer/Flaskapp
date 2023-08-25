FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt /app/

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2 \
    && pip install --no-cache-dir -r requirements.txt

COPY . /app/
