FROM python:3.8-buster

ADD src/ /app/
WORKDIR /app/

RUN pip install --upgrade pip \
    && pip install pipenv
RUN pipenv install --system

EXPOSE 8000

WORKDIR /app/
