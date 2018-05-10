"""
====== COMP90024 TEAM 16 ======

889545   Yu Liu          yul22       yul22@student.unimelb.edu.au
875095   Jize Dong       jized       jized@student.unimelb.edu.au
911764   Minsheng Wang   minshengw   minshengw@student.unimelb.edu.au
890742   Minglun Zhang   minglunz    minglunz@student.unimelb.edu.au
905084   Xingping Ding   xingpingd   xingpingd@student.unimelb.edu.au

"""

import boto
import key
from boto.ec2.regioninfo import RegionInfo


def connect():
    region = RegionInfo(name='melbourne-np', endpoint='nova.rc.nectar.org.au')

    access_idkey = key.key
    access_id = access_idkey.get_id(access_idkey)
    access_key = access_idkey.get_key(access_idkey)

    ec2_conn = boto.connect_ec2(aws_access_key_id=access_id, aws_secret_access_key=access_key, is_secure=True,
                                region=region, port=8773, path='/service/Cloud', validate_certs=False)
    return ec2_conn
