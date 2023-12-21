FROM python:3.11-alpine3.16

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /Django-Stripe/requirements.txt
COPY . .

WORKDIR ./

RUN pip install -r requirements.txt