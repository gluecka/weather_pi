#!/bin/bash

docker run -d -p 4000:8086 --restart=always --name=influxdb -v influxdb_data:/var/lib/docker/volumes/influxdb_data/_data -e DOCKER_INFLUXDB_INIT_MODE=setup -e DOCKER_INFLUXDB_INIT_USERNAME=<username> -e DOCKER_INFLUXDB_INIT_PASSWORD=<password> influxdb:1.8
