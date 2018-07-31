FROM ubuntu:18.04

ARG KEY_FILE

WORKDIR /app

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
ENV APP_CONFIGURING True

RUN apt-get update -qq
RUN apt-get install -yqq python3 python3-pip mysql-client libmysqlclient-dev wget git
RUN pip3 install pipenv

COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy
COPY . .
RUN make configure

# Download the Cloud SQL Proxy binary
RUN mkdir -p bin
RUN wget "https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64" -O "bin/cloud_sql_proxy" && chmod +x "bin/cloud_sql_proxy"
RUN mkdir /cloudsql && chmod 777 /cloudsql
# Generate start script
RUN echo "bin/cloud_sql_proxy -dir=/cloudsql -instances=\"insaction-71605:europe-west1:psql-main\"=tcp:3306 \
 -credential_file=bin/key_file.json &" > "bin/container_start.sh"
RUN echo "gunicorn -w 4 insaction.wsgi:application --bind=0.0.0.0:80" >> "bin/container_start.sh"
# Decode key file from environment vars
RUN echo $KEY_FILE | base64 -id > "bin/key_file.json"

EXPOSE 80

ENV APP_CONFIGURING False

CMD ["bash", "bin/container_start.sh"]
