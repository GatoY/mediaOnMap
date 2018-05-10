import json

"""
====== COMP90024 TEAM 16 ======

889545   Yu Liu          yul22       yul22@student.unimelb.edu.au
875095   Jize Dong       jized       jized@student.unimelb.edu.au
911764   Minsheng Wang   minshengw   minshengw@student.unimelb.edu.au
890742   Minglun Zhang   minglunz    minglunz@student.unimelb.edu.au
905084   Xingping Ding   xingpingd   xingpingd@student.unimelb.edu.au

"""

with open('../static/map/res/affordability20162017.geojson') as f:
    data = json.load(f)
    # print(aa['features'][0])
    data.pop("type")
    data.pop("bbox")
    data.pop("crs")
    features = data["features"]
    for feature in features:
        feature.pop("type")
        feature.pop("geometry")
        feature.pop("id")
    with open('../static/map/res/affordability_slim.json', 'w') as outFile:
        json.dump(data, outFile)
