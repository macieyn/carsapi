FROM python:3.8-buster

ADD src/ /app/
WORKDIR /app/
COPY Pipfile /app/
COPY Pipfile.lock /app/

RUN pip install --upgrade pip \
    && pip install pipenv
RUN pipenv install --system --skip-lock

EXPOSE 8000
