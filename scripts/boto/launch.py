import boto
import connect

def launch():
	conn = connect.connect()
	
    #NeCTAR Ubuntu 16.04 LTS (Xenial) amd64
	ami = 'ami-190a1773'
	reservation = conn.run_instances(ami, key_name = 'id_rsa', instance_type = 'm1.small', security_groups = ['default'])

	instance = reservation.instances[0]
	print('New instance {} has been created.'.format(instance.id))
