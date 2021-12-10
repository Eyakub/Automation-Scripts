#!/usr/bin/env bash

IMAGE_NAME="docker.elastic.co/elasticsearch/elasticsearch:7.12.0-amd64"
docker run -p 127.0.0.1:2048:2048 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.12.0-amd64
echo "=============elasticsearch running============"
docker run --name kib01-test --net elastic -p 127.0.0.1:4096:4096 -e "ELASTICSEARCH_HOSTS=http://es01-test:2048" docker.elastic.co/kibana/kibana:7.12.0

echo "=================kibana running============"
