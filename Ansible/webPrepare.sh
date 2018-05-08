#!/bin/bash
sudo su
source /home/ubuntu/env/bin/activate
cd /home/ubuntu/google-map-django-couchdb-jquery
pip install --upgrade pip
sudo /home/ubuntu/env/bin/pip install -r requirements.txt
mkdir static
/home/ubuntu/env/bin/python3 manage.py collectstatic
sudo /home/ubuntu/env/bin/pip install gunicorn

