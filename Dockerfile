FROM python:3.6.5-alpine3.6

WORKDIR /app

RUN pip install pipenv
COPY Pipfile Pipfile
RUN pipenv install
COPY . .

EXPOSE 80

CMD [ "make", "production" ]
