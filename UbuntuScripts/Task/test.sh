#!/usr/bin/env bash

if [ -x "$(command -v docker)" ]; then
	echo "okay"
fi
if [ $(docker inspect -f '{{.State.Running}}' $container_name) = "true" ]; then
	echo "docker running"
fi
