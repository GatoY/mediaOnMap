import boto
import connect

conn = connect.connect()
# Id of the instance u want to terminate
INSTANCE_ID = ''
conn.terminate_instances(instance_ids=[INSTANCE_ID])
