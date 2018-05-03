import boto
import key
from boto.ec2.regioninfo import RegionInfo 

def connect():
	region = RegionInfo(name = 'melbourne-np', endpoint = 'nova.rc.nectar.org.au')

	access_idkey = key.key
	access_id = access_idkey.get_id(access_idkey)
	access_key = access_idkey.get_key(access_idkey)

	ec2_conn = boto.connect_ec2(aws_access_key_id = access_id, aws_secret_access_key = access_key, is_secure = True,
		region = region, port = 8773, path = '/service/Cloud', validate_certs = False)
	return ec2_conn
