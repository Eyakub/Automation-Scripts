#!/bin/sh

if [[ "$(docker images -q elesticsearch 2> /dev/null)" != "" ]]; then
  echo "Elasticsearch found..."
  #   docker run -p 127.0.0.1:9200:9200 -p 127.0.0.1:9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.15.2
  docker run -p 127.0.0.1:2048:2048 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.12
  if [[ "$(docker images -q kibana 2> /dev/null)" != "" ]]; then
    echo "Kibana found..."
    docker network create elastic
    docker run --name kib01-test --net elastic -p 127.0.0.1:4096:4096 -e "ELASTICSEARCH_HOSTS=http://es01-test:9200" docker.elastic.co/kibana/kibana:7.12
    fi
fi

