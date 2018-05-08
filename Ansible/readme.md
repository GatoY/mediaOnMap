#Attention
When setup web server, due to ALLOWED_HOSTS in settings.py is null, make sure u add ur ip of instances or domain name.
In case if it doesn't work, 
/bin/bash: sudo service nginx reload
/bin/bash: sudo gunicorn --bind unix:/tmp/catsnevercode.club.socket mediaMap.wsgi:application --reload&

