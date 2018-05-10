#
# ========================= COMP90024 TEAM 16 =========================
#
# 889545   Yu Liu          yul22       yul22@student.unimelb.edu.au
# 875095   Jize Dong       jized       jized@student.unimelb.edu.au
# 911764   Minsheng Wang   minshengw   minshengw@student.unimelb.edu.au
# 890742   Minglun Zhang   minglunz    minglunz@student.unimelb.edu.au
# 905084   Xingping Ding   xingpingd   xingpingd@student.unimelb.edu.au
#
# =====================================================================
#


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

