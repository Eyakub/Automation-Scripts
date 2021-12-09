#!/usr/bin/env bash

install_docker() {
    echo "Updating..."
    sudo apt-get update
    
    echo "Installing required dependencies..."
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
    sudo apt-get install docker-ce docker-ce-cli containerd.io
    sudo systemctl start docker
    if [ -x "$(command -v docker)" ]; then
        echo "Docker is installed..."
        docker pull docker.elastic.co/elasticsearch/elasticsearch:7.5.2
        docker pull docker.elastic.co/kibana/kibana:7.5.2

    else
        echo "Docker is not installed"
    fi
}

# if docker any older version of docker installed, uninstall it first
if [ -x "$(command -v docker)" ]; then
    echo "Docker is already installed"
    sudo apt-get purge -y docker docker-engine docker.io docker-ce docker-ce-cli containerd runc
    sudo rm -rf /var/lib/docker
    sudo rm -rf /var/lib/containerd
    echo "Docker is removed, re-installing docker again..."
    install_docker
else
    echo "calling install docker function..."
    install_docker
fi
