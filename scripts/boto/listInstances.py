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

conn = connect.connect()

reservations = conn.get_all_reservations()
print('Index\tID\t\tInstance')
for idx, res in enumerate(reservations):
    print('{}\t{}\t{}'.format(idx, res.id, res.instances))
    print('\nID: {}\tIP: {}\tPlacement: {}'.format(reservations[0].id, reservations[0].instances[0].private_ip_address,
                                                   reservations[0].instances[0].placement))
