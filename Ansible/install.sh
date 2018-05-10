#!/bin/bash

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

sudo su

# varibles
export local_ip=`ifconfig eth0 | grep 'inet addr' | cut -b 21-34`
export user=admin
export passwd=admin


# couchdb establishment
docker pull couchdb:2.1.1

docker create -v /mnt/database:/opt/couchdb/data -p 5984:5984 -p 4369:4369 -p 5986:5986 -p 9100-9200:9100-9200 --net=host couchdb:2.1.1
sleep 3

export container_id=`docker ps -all | grep couchdb | cut -f1 -d' '`
sleep 3

docker start ${container_id}
sleep 3

docker exec ${container_id} bash -c "echo \"-setcookie couchdb_cluster\" >> /opt/couchdb/etc/vm.args"

docker exec ${container_id} bash -c "echo \"-name couchdb@${local_ip}\" >> /opt/couchdb/etc/vm.args"
sleep 3

docker restart ${container_id} 
sleep 3

curl -X PUT "http://${local_ip}:5984/_node/_local/_config/admins/${user}" --data "\"${passwd}\""

curl -X PUT "http://${user}:${passwd}@${local_ip}:5984/_node/couchdb@${local_ip}/_config/chttpd/bind_address" --data '"0.0.0.0"'
