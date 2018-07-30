FROM python:3.6.5-alpine3.7

WORKDIR /app

RUN pip install pipenv
COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy
COPY . .
RUN make configure

EXPOSE 80

CMD [ "make", "production" ]
