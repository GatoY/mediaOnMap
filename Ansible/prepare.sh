#!/bin/bash
sudo su
apt-get update
apt-get -y install vim
apt-get -y install docker.io

# mount volume
mkfs.ext4 /dev/vdc
mkdir /mnt/database
touch /mnt/database/couchdb
mount /dev/vdc /mnt/database

