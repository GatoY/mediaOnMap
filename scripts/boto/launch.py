"""
====== COMP90024 TEAM 16 ======

889545   Yu Liu          yul22       yul22@student.unimelb.edu.au
875095   Jize Dong       jized       jized@student.unimelb.edu.au
911764   Minsheng Wang   minshengw   minshengw@student.unimelb.edu.au
890742   Minglun Zhang   minglunz    minglunz@student.unimelb.edu.au
905084   Xingping Ding   xingpingd   xingpingd@student.unimelb.edu.au

"""

import boto
import connect


def launch():
    conn = connect.connect()

    # NeCTAR Ubuntu 16.04 LTS (Xenial) amd64
    ami = 'ami-190a1773'
    reservation = conn.run_instances(ami, key_name='id_rsa', instance_type='m1.small', security_groups=['default'])

    instance = reservation.instances[0]
    print('New instance {} has been created.'.format(instance.id))
