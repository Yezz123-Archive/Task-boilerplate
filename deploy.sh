#!/bin/bash

echo "Enter mysql root password"
read -s password

docker network create task-network
docker volume create volume

docker build -t db db
docker build -t flask-app flask-app

docker run -d --network task-network --mount type=volume,source= volume,target=/var/lib/mysql -e MYSQL_ROOT_PASSWORD=$password --name mysql db
docker run -d --network task-network -e password=$password --name flask-app flask-app
docker run -d --network task-network --mount type=bind,source=$(pwd)/nginx/nginx.conf,target=/etc/nginx/nginx.conf -p 80:80 --name nginx nginx:alpine
