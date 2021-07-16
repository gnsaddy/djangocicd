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

echo "----------------------------------------"
python3 manage.py migrate

python3 manage.py makemigrations
echo "----------------------------------------"

python3 manage.py migrate
echo "----------------------------------------"

sudo killall nginx
sudo systemctl restart nginx
sudo service nginx restart