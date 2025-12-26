#!/bin/sh
# . venv/bin/activate # Not needed in Docker as we install to system

while true; do
    flask deploy
    if [ "$?" -eq 0 ]; then
        break
    fi
    echo Deploy command failed, retrying in 5 secs...
    sleep 5
done

exec gunicorn -b :5000 --access-logfile - --error-logfile - flasky:app
