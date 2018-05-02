import boto
import connect

conn = connect.connect()

reservations = conn.get_all_reservations()
print('Index\tID\t\tInstance')
for idx, res in enumerate(reservations):
	print('{}\t{}\t{}'.format(idx, res.id, res.instances))
	print('\nID: {}\tIP: {}\tPlacement: {}'.format(reservations[0].id, reservations[0].instances[0].private_ip_address, reservations[0].instances[0].placement))
