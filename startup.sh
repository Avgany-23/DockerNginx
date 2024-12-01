#!/bin/bash

docker network create project_bridge

docker build -f nginx/Dockerfile . -t nginx_image
docker run -d --name nginx_cont -p 80:80 --network project_bridge -v static_volume:/usr/src/app/static nginx_image

docker build -f db/Dockerfile . -t db_image
docker run -d --name db_cont -v data_volume:/var/lib/data_psql -p 5432:5432 --network project_bridge db_image

docker build -f project/Dockerfile project -t project_image
docker run \
    --name project_cont \
    -v static_volume:/usr/src/app/static \
    -e DB_HOST=db_cont \
    -e PROJECT_HOST=192.168.0.110 \
    -p 8000:8000 \
    -d \
    --network project_bridge \
    project_image
