FROM python:3.8-buster

ENV PYTHONUNBUFFERED=1
ENV DJANGO_KEY==0ay5hg4ee_em4+s-(@y4csvnyks)b6i8sxvjlwc*e)fa_w(%=

WORKDIR /app/
ADD cars/ cars/
ADD cars_api/ cars_api/
ADD static/ static/

COPY wait-for-it.sh .
RUN chmod +x wait-for-it.sh
COPY manage.py .
COPY Pipfile .
COPY Pipfile.lock .

RUN pip install --upgrade pip \
    && pip install pipenv
RUN pipenv install --skip-lock --system
RUN python manage.py generateschema --file openapi-schema.yml

EXPOSE 8000
