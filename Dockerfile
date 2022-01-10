# Pull a pre-built alpine docker image with nginx and python3 installed
FROM tiangolo/uwsgi-nginx:python3.8-alpine

ENV LISTEN_PORT=8000
EXPOSE 8000

# Indicate where uwsgi.ini lives
ENV UWSGI_INI uwsgi.ini


ENV STATIC_URL /app/static_collected


WORKDIR /app
ADD . /app


RUN chmod g+w /app
RUN chmod g+w /app/db.sqlite3

# Make sure dependencies are installed
RUN python3 -m pip install -r requirements.txt