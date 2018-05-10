import json

"""
====== COMP90024 TEAM 16 ======

889545   Yu Liu          yul22       yul22@student.unimelb.edu.au
875095   Jize Dong       jized       jized@student.unimelb.edu.au
911764   Minsheng Wang   minshengw   minshengw@student.unimelb.edu.au
890742   Minglun Zhang   minglunz    minglunz@student.unimelb.edu.au
905084   Xingping Ding   xingpingd   xingpingd@student.unimelb.edu.au

"""

with open('../static/map/img/trafficComplaintsByHours.json') as f:
    data = json.load(f)
    result = {}
    for row in data["rows"]:
        result[(int(row["key"]) + 10) % 24] = row["value"]

    with open('../static/map/res/traffic_by_hours.json', 'w') as outFile:
        json.dump(result, outFile)
