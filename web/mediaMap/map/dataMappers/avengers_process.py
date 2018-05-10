import json

"""
====== COMP90024 TEAM 16 ======

889545   Yu Liu          yul22       yul22@student.unimelb.edu.au
875095   Jize Dong       jized       jized@student.unimelb.edu.au
911764   Minsheng Wang   minshengw   minshengw@student.unimelb.edu.au
890742   Minglun Zhang   minglunz    minglunz@student.unimelb.edu.au
905084   Xingping Ding   xingpingd   xingpingd@student.unimelb.edu.au

"""

with open('../static/map/img/theAvengers.json') as f:
    data = json.load(f)

    result = {}

    for entry in data["rows"]:
        if entry["key"][0] not in result.keys():
            result[entry["key"][0]] = {"positive": 0, "negative": 0, "neutral": 0}
        result[entry["key"][0]][entry["key"][1]] = entry["value"]
    for key in result:
        result[key]["total"] = result[key]["positive"] + result[key]["negative"] + result[key]["neutral"]

    with open('../static/map/res/avengers.json', 'w') as outFile:
        json.dump(result, outFile)
