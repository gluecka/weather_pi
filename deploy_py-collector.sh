#!/bin/bash

docker run -d --privileged=true --name=py-collector --restart=always -v /etc/localtime:/etc/localtime collector:1.0
