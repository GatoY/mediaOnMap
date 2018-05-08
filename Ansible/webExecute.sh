#!/bin/bash
sudo su
service nginx start
gunicorn --bind unix:/tmp/catsnevercode.club.socket mediaMap.wsgi:application&
