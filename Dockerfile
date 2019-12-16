FROM tiangolo/uwsgi-nginx-flask:python3.6-index

ENV STATIC_URL /app/static
ENV STATIC_APP /app/app/static


RUN apt-get -q update && apt-get install -qy netcat

COPY ./bin/wait-for /usr/bin

RUN chmod +x /usr/bin/wait-for

COPY ./requirements.txt /app/requirements.txt

RUN  pip install -r /app/requirements.txt

COPY . /app/

WORKDIR /app

