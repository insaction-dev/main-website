FROM ubuntu:18.04

WORKDIR /app

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV APP_SECRET_KEY "not_a_secret_key"

RUN uname -a
RUN apt-get update
RUN apt-get install python3 python3-pip make mysql-client libmysqlclient-dev -y

RUN pip3 install pipenv
COPY Pipfile Pipfile.lock ./
RUN pipenv install --deploy
COPY . .
RUN pipenv run python manage.py collectstatic --no-input

EXPOSE 8080

CMD [ "make", "production" ]
