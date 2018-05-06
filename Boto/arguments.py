import boto
from boto.ec2.regioninfo import RegionInfo
import time
import argparse

access_key_id = ''
secret_access_key = ''

parser =argparse.ArgumentParser()

# ACCESS_KEY_ID
parser.add_argument('-k','--key')
# SECRET_ACCESS_KEY
parser.add_argument('-s','--secret')
# The number of instances to create
parser.add_argument('-l','--launch')
# The capacity of volume.
parser.add_argument('-v','--volume')
# Instance id to terminate
parser.add_argument('-t','--terminate')

args=parser.parse_args()

access_key_id = args.key
secret_access_key = args.secret
numOfInstances = args.launch
capOfVolume = args.volume
instanceToTerm = args.terminate

# Connect ec2
def connect_ec2(access_key_id, secret_access_key):
	region = RegionInfo(name='melbourne', endpoint='nova.rc.nectar.org.au')
	ec2_conn = boto.connect_ec2(aws_access_key_id=access_key_id, 
		aws_secret_access_key=secret_access_key,
		is_secure=True, 
		region=region,
		port=8773,
		path='/services/Cloud', 
		validate_certs=False)

	print('Connect ec2 successfully.')

	return ec2_conn

# Launch instances
def launch_instances(ec2_conn, numOfInstances):
	reservations = []
	for i in range(numOfInstances):
		reservation = ec2_conn.run_instances('ami-00003837', 
			key_name='cloud',
			security_groups=['default'],
			instance_type='m1.medium',
			placement="melbourne-qh2")
		reservations.append(reservation)

	print('Lunch instances successfully.')

	return reservations

# Terminate instances
def terminate_instances(ec2_conn):
	reservations = ec2_conn.get_all_reservations()
	instance_ids = []
	for reservation in reservations:
		for instance in reservation.instances:
			instance_ids.append(instance.id)

	if len(instance_ids) > 0:
		ec2_conn.terminate_instances(instance_ids=instance_ids)

	print('Terminate instances successfully.')

def terminateById(ec2_conn, instanceToTerm):
	reservations = ec2_conn.get_all_reservations()
	try:
		ec2_conn.terminate_instances(instance_ids=instance_ids)
		print('Terminate instances successfully.')
	except:
		print("Incorrect ID")
	
# Show instances detail
def show_instances_detail(ec2_conn):
	reservations = ec2_conn.get_all_reservations()
	for reservation in reservations:
		print('\nID: {}\tIP: {}\tPlacement: {}'.format(reservation.instances[0].id, reservation.instances[0].private_ip_address,reservation.instances[0].placement))

# Create volume
def create_volumes(ec2_conn, capacity):
	volumes = []
	for i in range(INSTANCE_COUNT):
		volume = ec2_conn.create_volume(capacity, 'melbourne-qh2')
		volumes.append(volume)
	print('Create volumes successfully.')
	return volumes

# Attach volume
def attach_volume(ec2_conn, volumes, reservations):
	for i in range(INSTANCE_COUNT):
		# Wait for instance runing
		for instance in reservations[i].instances:
			while instance.state != 'running':
				time.sleep(2)
				instance.update()

		ec2_conn.attach_volume(volumes[i].id, reservations[i].instances[0].id, '/dev/vdc')
	print('Attach volumes successfully.')

def main():
	ec2_conn = connect_ec2(access_key_id, secret_access_key)
	if(numOfInstances):
		reservations = launch_instances(ec2_conn, numOfInstances)
		if(capacity):
			volumes = create_volumes(ec2_conn, capacity)
			attach_volume(ec2_conn, volumes, reservations)
		show_instances_detail(ec2_conn)
	if(instanceToTerm):
		if(instanceToTerm='a'):
			terminate_instances(ec2_conn)
		else:
			terminateById(ec2_conn, instanceToTerm)

if __name__ == '__main__':
	main()