import boto
import connect

def list_images():
	conn = connect.connect()
	images = conn.get_all_images()
	for img in images:
		print('Image id: {}, image name: {}'.format(img.id, img.name))
