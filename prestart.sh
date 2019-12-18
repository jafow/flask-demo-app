#!/usr/bin/env bash
#
# prestart.sh: called by docker parent image https://github.com/tiangolo/uwsgi-nginx-flask-docker
# Apply db migrations after wait-for connection to db established
# load initial data for members

echo "applying migrations"
echo "===================="

max_retry_count=5
count=0

while true; do
    if [ $count -gt $max_retry_count ]; then
      exit 1
    fi

    flask db upgrade
    if [ "$?" -eq 0 ]; then
        break
    fi
    echo migrations failed, retrying in 5 secs...
    count=$((count+1))
    sleep 5
done

echo "members ======================================================="
python manage.py loadmembers
echo "members ======================================================="
