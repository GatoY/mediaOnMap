#!/bin/bash
# master only

sudo su

export slave_node1=115.146.85.220
export slave_node2=115.146.85.235
export uname=admin
export passwd=admin

curl -X POST -H 'Content-Type: application/json' http://${uname}:${passwd}@127.0.0.1:5984/_cluster_setup -d "{\"action\": \"enable_cluster\", \"bind_address\":\"0.0.0.0\", \"username\": \"${uname}\", \"password\":\"${passwd}\", \"port\": 5984, \"node_count\": \"3\", \"remote_node\": \"${slave_node1}\", \"remote_current_user\": \"${uname}\", \"remote_current_password\": \"${passwd}\"}"

curl -X POST -H 'Content-Type: application/json' http://${uname}:${passwd}@127.0.0.1:5984/_cluster_setup -d "{\"action\": \"add_node\", \"host\":\"${slave_node1}\", \"port\": 5984, \"username\": \"admin\", \"password\":\"admin\"}"


curl -X POST -H 'Content-Type: application/json' http://${uname}:${passwd}@127.0.0.1:5984/_cluster_setup -d "{\"action\": \"enable_cluster\", \"bind_address\":\"0.0.0.0\", \"username\": \"${uname}\", \"password\":\"${passwd}\", \"port\": 5984, \"node_count\": \"3\", \"remote_node\": \"${slave_node2}\", \"remote_current_user\": \"${uname}\", \"remote_current_password\": \"${passwd}\"}"

curl -X POST -H 'Content-Type: application/json' http://${uname}:${passwd}@127.0.0.1:5984/_cluster_setup -d "{\"action\": \"add_node\", \"host\":\"${slave_node2}\", \"port\": 5984, \"username\": \"${uname}\", \"password\":\"${passwd}\"}"
