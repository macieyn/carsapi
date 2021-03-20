FROM python:3.8-buster

ENV PYTHONUNBUFFERED=1
ENV DJANGO_KEY==0ay5hg4ee_em4+s-(@y4csvnyks)b6i8sxvjlwc*e)fa_w(%=

ADD cars/ /app/cars/
ADD cars_api/ /app/cars_api/
ADD static/ /app/static/

COPY manage.py /app/
COPY Pipfile /app/
COPY Pipfile.lock /app/
WORKDIR /app/

RUN pip install --upgrade pip \
    && pip install pipenv
RUN pipenv install --skip-lock --system
RUN python manage.py generateschema --file openapi-schema.yml

EXPOSE 8000
