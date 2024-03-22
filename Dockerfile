FROM python:3.9-alpine
ENV PYTHONUNBUFFERED=1
WORKDIR /django/core
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY /core .