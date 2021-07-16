#!/bin/bash
echo "Starting env"
source ~/env/bin/activate
echo "Env activated"
source ~/env/bin/activate
pwd
pip3 freeze
ls
cd /home/ubuntu/djangocicd

sudo apt install apt-transport-https ca-certificates curl software-properties-common

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"

sudo apt update -y

sudo apt install docker-ce -y

sudo usermod -aG docker ${USER}
su - ${USER}
sudo usermod -aG docker username
sudo service docker start
