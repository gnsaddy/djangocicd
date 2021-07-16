#!/bin/bash

echo "Starting env"
source ~/env/bin/activate
echo "Env activated"
source ~/env/bin/activate
pwd
pip3 freeze
ls
cd /home/ubuntu/djangocicd
echo "----------------------------------------"
pwd
echo "----------------------------------------"
sudo pip3 install -r requirements.txt