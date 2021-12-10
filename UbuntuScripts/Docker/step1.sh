#!/usr/bin/env bash

install_docker() {
    echo "Updating..."
    sudo apt-get update
    
    echo "Installing required dependencies..."
    sudo dpkg --configure -a
    sudo apt-get install -f
    sudo apt-get install \
                ca-certificates \
                curl \
                gnupg \
                lsb-release \
    
    echo "Installing docker..."

    # add dockers oficial GPG key
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

    echo \
        "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
        $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    
    sudo apt-get update
    sudo apt-get install -y docker-ce docker-ce-cli containerd.io
    sudo systemctl start docker
    sudo systemctl enable docker
    sudo systemctl restart docker
    if [ -x "$(command -v docker)" ]; then
        echo "Docker is installed..."
        docker pull docker.elastic.co/elasticsearch/elasticsearch:7.12.0-amd64
        docker pull docker.elastic.co/kibana/kibana:7.12.0

        if [[ "$(docker images -q 'docker.elastic.co/elasticsearch/elasticsearch:7.12.0-amd64'  2> /dev/null)" != "" ]]; then
            echo "Elesticsearch image found..."
            docker network create elastic
            docker run -d --name es01-test --net elastic -p 2048:2048 -p 3048:3048 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.12.0-amd64
        else
            echo "Elesticsearch image not found..."
        fi

        if [[ "$(docker images -q 'docker.elastic.co/kibana/kibana:7.12.0'  2> /dev/null)" != "" ]]; then
            echo "kibana image found..."
            docker run -d --name kib01-test --net elastic -p 4096:4096 -e "ELASTICSEARCH_HOSTS=http://es01-test:2048" docker.elastic.co/kibana/kibana:7.12.0
        fi

    else
        echo "Docker is not installed"
    fi
}

# if docker any older version of docker installed, uninstall it first
if [ -x "$(command -v docker)" ]; then
    echo "Docker is already installed"
    sudo systemctl docker stop
    sudo apt-get remove --purge -y docker docker-engine docker.io docker-ce docker-ce-cli containerd runc
    sudo apt-get autoremove -y --purge docker-engine docker docker.io docker-ce  
    sudo rm -rf /var/lib/docker /etc/docker
    sudo rm /etc/apparmor.d/docker
    sudo groupdel docker
    sudo rm -rf /var/run/docker.sock
    sudo rm -rf /var/lib/docker
    sudo rm -rf /var/lib/containerd
    sudo apt clean
    sudo apt autoremove
    echo "Docker is removed, re-installing docker again..."
    install_docker
else
    echo "calling install docker function..."
    install_docker
fi
