FROM python:3.9-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONBUFFERED 1

COPY ./requirements.txt /app/requirements.txt

RUN python3 -m pip install -r /app/requirements.txt --no-cache-dir

COPY ./app /app/