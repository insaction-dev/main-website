FROM python:3.6.5-alpine3.6

WORKDIR /app

RUN pip install pipenv
COPY Pipfile Pipfile
RUN pipenv install --system
COPY . .

EXPOSE 80
