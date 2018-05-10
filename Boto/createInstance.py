"""
========================= COMP90024 TEAM 16 =========================

889545   Yu Liu          yul22       yul22@student.unimelb.edu.au
875095   Jize Dong       jized       jized@student.unimelb.edu.au
911764   Minsheng Wang   minshengw   minshengw@student.unimelb.edu.au
890742   Minglun Zhang   minglunz    minglunz@student.unimelb.edu.au
905084   Xingping Ding   xingpingd   xingpingd@student.unimelb.edu.au

=====================================================================

"""

import boto
from boto.ec2.regioninfo import RegionInfo
import time

# The number of instances to create
INSTANCE_COUNT = 1

ACCESS_KEY_ID = '309ec20dc3f2441e8d23d7a65806a7b8'
SECRET_ACCESS_KEY = '5c7418ac22cd433a9c77a26ec7fbbc39'


# Connect ec2
def connect_ec2():
    region = RegionInfo(name='melbourne', endpoint='nova.rc.nectar.org.au')
    ec2_conn = boto.connect_ec2(aws_access_key_id=ACCESS_KEY_ID,
                                aws_secret_access_key=SECRET_ACCESS_KEY,
                                is_secure=True,
                                region=region,
                                port=8773,
                                path='/services/Cloud',
                                validate_certs=False)

    print('Connect ec2 successfully.')

    return ec2_conn


# Launch instances
def launch_instances(ec2_conn):
    reservations = []
    for i in range(INSTANCE_COUNT):
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


# Show instances detail
def show_instances_detail(ec2_conn):
    reservations = ec2_conn.get_all_reservations()
    for reservation in reservations:
        print('\nID: {}\tIP: {}\tPlacement: {}'.format(reservation.instances[0].id,
                                                       reservation.instances[0].private_ip_address,
                                                       reservation.instances[0].placement))


# Create volume
def create_volumes(ec2_conn):
    volumes = []
    for i in range(INSTANCE_COUNT):
        volume = ec2_conn.create_volume(60, 'melbourne-qh2')
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
    ec2_conn = connect_ec2()
    reservations = launch_instances(ec2_conn)
    volumes = create_volumes(ec2_conn)
    attach_volume(ec2_conn, volumes, reservations)
    show_instances_detail(ec2_conn)


# terminate_instances(ec2_conn)

if __name__ == '__main__':
    main()
