
#Web Server
##Introduction
This project is for visualizing the results of analysis of Twitter data located in Melbourne.
##Prerequisites
ansible==2.5.2
Ubuntu 16.04 on AWS
##Files structure
default: Nginx config file.
webPrepare.sh: bash script for installing packages.
web Execute.sh: run server
##Usage

    ansible-playbook web.yml
    
##Attention
When setup web server, due to ALLOWED_HOSTS in settings.py is null, make sure u add ur ip of instances or domain name.
In case if it doesn't work, 

    #bash: source /home/ubuntu/env/bin/activate
    #bash: sudo service nginx reload
    #bash: sudo gunicorn --bind unix:/tmp/catsnevercode.club.socket mediaMap.wsgi:application --reload&

