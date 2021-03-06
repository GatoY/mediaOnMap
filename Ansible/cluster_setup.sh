#!/bin/bash
# master only

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

export slave_node1=115.146.85.235
export slave_node2=115.146.85.237
export uname=admin
export passwd=admin

curl -X POST -H 'Content-Type: application/json' http://${uname}:${passwd}@127.0.0.1:5984/_cluster_setup -d "{\"action\": \"enable_cluster\", \"bind_address\":\"0.0.0.0\", \"username\": \"${uname}\", \"password\":\"${passwd}\", \"port\": 5984, \"node_count\": \"3\", \"remote_node\": \"${slave_node1}\", \"remote_current_user\": \"${uname}\", \"remote_current_password\": \"${passwd}\"}"

curl -X POST -H 'Content-Type: application/json' http://${uname}:${passwd}@127.0.0.1:5984/_cluster_setup -d "{\"action\": \"add_node\", \"host\":\"${slave_node1}\", \"port\": 5984, \"username\": \"admin\", \"password\":\"admin\"}"


curl -X POST -H 'Content-Type: application/json' http://${uname}:${passwd}@127.0.0.1:5984/_cluster_setup -d "{\"action\": \"enable_cluster\", \"bind_address\":\"0.0.0.0\", \"username\": \"${uname}\", \"password\":\"${passwd}\", \"port\": 5984, \"node_count\": \"3\", \"remote_node\": \"${slave_node2}\", \"remote_current_user\": \"${uname}\", \"remote_current_password\": \"${passwd}\"}"

curl -X POST -H 'Content-Type: application/json' http://${uname}:${passwd}@127.0.0.1:5984/_cluster_setup -d "{\"action\": \"add_node\", \"host\":\"${slave_node2}\", \"port\": 5984, \"username\": \"${uname}\", \"password\":\"${passwd}\"}"
