#!/bin/bash

source env/bin/activate

# cd ~/djangocicd

pip3 install -r requirements.txt

python3 manange.py makemigrations

python3 manage.py migrate
