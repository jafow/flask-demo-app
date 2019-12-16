#!/usr/bin/env bash
set -e

echo "applying migrations"

max_retry_count=5
count=0

while true; do
    if [[ $count -gt $max_retry_count ]]; then
      exit 1
    fi

    flask db upgrade
    if [[ "$?" == "0" ]]; then
        break
    fi
    echo migrations failed, retrying in 5 secs...
    count=$((count+1))
    sleep 5
done
