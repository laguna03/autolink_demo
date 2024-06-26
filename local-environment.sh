#!/bin/bash

set -e # exit when any command fails

current_path="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

# stop containers
echo "stopping containers"
docker-compose -f "$current_path/docker-compose.yml" down
if [ "$1" == "--local-environment-compose" ]; then
    echo 'Local Environment Compose Mode'
    docker-compose -f "local-environment-compose/docker-compose.yml" down
fi

# start containers
echo "starting containers"
if [ "$1" == "--local-environment-compose" ]; then
    echo 'Local Environment Compose Mode'
    docker-compose -f "local-environment-compose/docker-compose.yml" up -d --build
fi
docker-compose -f "$current_path/docker-compose.yml" up -d --build
