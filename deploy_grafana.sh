#!/bin/bash

docker run -d -p 3000:3000 --restart=always --name=grafana -v grafana_storage:/var/lib/docker/volumes/grafana_storage/_data grafana/grafana:latest
