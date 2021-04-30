FROM        python:3.8.1-alpine3.11
WORKDIR     /usr/src/app
ENV         POETRY_VIRTUALENVS_CREATE=false
ENV         PATH=/root/.poetry/bin:$PATH
ENV         PATH=/root/.local/bin/:$PATH
COPY        . .
# RUN         apk add postgresql-dev \
#                     build-base

RUN         apk add curl && \
            curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python - && \
            poetry install -vv -n --no-dev


# FROM        python:3.8.1-alpine3.11 AS builder
# WORKDIR     /usr/src/app
# ADD         requirements.txt .
# RUN         apk add postgresql-dev \
#                     build-base
# RUN         pip install -r requirements.txt
#
# ###
# FROM        python:3.8.1-alpine3.11
# WORKDIR     /usr/src/app/
#
# ENV         FLASK_APP=manage.py
# COPY        --from=builder /usr/local /usr/local
# COPY        . .
