FROM python:3.10-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /app

ADD requirements.txt /app

ADD . /app

RUN pip install -r /app/requirements.txt