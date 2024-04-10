FROM python:3.11

WORKDIR /app

COPY requirements/ requirements/

RUN pip install -r requirements/local.txt

COPY ./ /app/