"""
====== COMP90024 TEAM 16 ======

889545   Yu Liu          yul22       yul22@student.unimelb.edu.au
875095   Jize Dong       jized       jized@student.unimelb.edu.au
911764   Minsheng Wang   minshengw   minshengw@student.unimelb.edu.au
890742   Minglun Zhang   minglunz    minglunz@student.unimelb.edu.au
905084   Xingping Ding   xingpingd   xingpingd@student.unimelb.edu.au

"""


class key():
    my_access_key_id = ''
    my_secret_access_key = ''

    def __init__(self):
        pass

    def get_id(self):
        return self.my_access_key_id

    def get_key(self):
        return self.my_secret_access_key
