#!/bin/bash

echo "Starting env"
source ~/env/bin/activate
echo "Env activated"
source ~/env/bin/activate
pwd
pip3 freeze

pip3 install -r ~/djangocicd/requirements.txt