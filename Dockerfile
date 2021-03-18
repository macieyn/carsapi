FROM python:3.8-buster

ADD cars/ /app/cars/
ADD cars_api/ /app/cars_api/

COPY manage.py /app/
COPY Pipfile /app/
COPY Pipfile.lock /app/
WORKDIR /app/

RUN pip install --upgrade pip \
    && pip install pipenv
RUN pipenv install --skip-lock --system

EXPOSE 8000
