import boto
import connect

conn = connect.connect()
vol_req = conn.create_volume(5, 'melbourne')

curr_vols = con.get_all_volumes([vol_req.id])

#print('Volume status: {}, volume AZ: {}'.format(curr_vols[0].status, curr_vols[0].zone))
instanceId = ''
conn.attach_volume(vol_req.id, instanceId, '/dev/vdc')
print('ok')
