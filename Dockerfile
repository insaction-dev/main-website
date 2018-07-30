FROM ubuntu:18.04

WORKDIR /app

RUN apt-get install python3 python3-pip mysql-client libmysqlclient-dev
RUN pip3 install pipenv

COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy
COPY . .
RUN python3 manage.py collectstatic --no-input

EXPOSE 80

ENV DJANGO_SETTINGS_MODULE insaction.settings.prod

CMD ["gunicorn", "-w", "4", "insaction.wsgi:application"]
