import boto
import connect

conn = connect.connect()
images = conn.get_all_images()
for img in images:
	print('Image id: {}, image name: {}'.format(img.id, img.name))
