FROM python:3.11

WORKDIR /app

COPY requirements/ requirements/

RUN pip install -r requirements/production.txt

COPY ./ /app/