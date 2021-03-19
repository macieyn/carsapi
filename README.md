# Cars API

#### Intro

Stack: Django, Django Rest Framework, PostgreSQL, Docker

App was written according to the [specification](SPECS.md).

#### How to start an app

Application is fully dockerized. To start an application run `docker-compose up`.

`docker-compose.yml` pulls an image for Postgres 13.2 and Python 3.8.

#### Description

Chosen Python version is 3.8, since it has full support until April 2021 and security support until October 2024.
Probably not the best choice - maybe 3.9 is a go version - but 3.8 is supported by almost all third party packages.

My choice for database was SQLite for early development and PostgreSQL for production. Using Postgres was convinient choice when hosting app with Heroku.

As much as possible was written with abstractions provided by django and DRF.

#### Third party packages
- `Django Rest Framework` - simplifies the process of serializing and validating data, good support, mature package
- `requests` - reasonable choice for making API calls to third party APIs, good support, mature package
- `psycopg2-binary` - required for connection to Postgres
- `dj-database-url` - unables to use url string to connect to database
- `black` - code formatter, helps in keeping codebase consistent with PEP8 
- `gunicorn` - required by heroku
- `whitenoise` - helps in serving staticfiles in production

#### Testing

For testing was used django builtin testing framework and it follow OOP paradigm.

Tests for models are separated from API tests.

API tests are testing response status codes and data returned by endpoints and methods mentioned in specification. To be sure, not allowed method are tested if they are returning 405 status code.

#### Errors

Some fields required custom validation. If request is sending field that can not be validated, it returns name of that field as a key and a message with error details. This follows default DRF schema for validation errors.

