# /bin/bash
set -e # exit when any command fails

echo '::: Init :::'


if [ -z "$ENVIRONMENT_NAME" ]; then
    echo 'Environment Variable ENVIRONMENT_NAME is not defined. Setting to ENVIRONMENT_NAME=waiting'
    export ENVIRONMENT_NAME="waiting"
fi

if [ "$ENVIRONMENT_NAME" == "waiting" ]; then
    echo '::: Waiting :::'
    while true; do 
    echo "Waiting..."
    sleep 1800; 
    done;
fi

if [ "$ENVIRONMENT_NAME" == "local" ]; then
    echo '::: API | local :::'
    cd api
    pipenv run uvicorn main:app --host 0.0.0.0 --port 8080 --reload
fi

if [ "$ENVIRONMENT_NAME" == "dev" ]; then
    echo '::: API | dev :::'
    cd api
    pipenv run uvicorn main:app --host 0.0.0.0 --port 80
fi

if [ "$ENVIRONMENT_NAME" == "stage" ]; then
    echo '::: API | stage :::'
    cd api
    pipenv run uvicorn main:app --host 0.0.0.0 --port 80
fi

if [ "$ENVIRONMENT_NAME" == "prod" ]; then
    echo '::: API | prod :::'
    cd api
    pipenv run uvicorn main:app --host 0.0.0.0 --port 80
fi