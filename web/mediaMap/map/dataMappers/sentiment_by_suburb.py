import json

"""
====== COMP90024 TEAM 16 ======

889545   Yu Liu          yul22       yul22@student.unimelb.edu.au
875095   Jize Dong       jized       jized@student.unimelb.edu.au
911764   Minsheng Wang   minshengw   minshengw@student.unimelb.edu.au
890742   Minglun Zhang   minglunz    minglunz@student.unimelb.edu.au
905084   Xingping Ding   xingpingd   xingpingd@student.unimelb.edu.au

"""

with open('../static/map/img/sentiment_by_suburbs.geojson') as f:
    geojson = json.load(f)

    for feature in geojson["features"]:
        properties = feature["properties"]

        sentiment = properties["pos_rate"]

        if sentiment is None:
            properties["color"] = "#666666"
        elif float(sentiment) < 0.2:
            properties["color"] = "#FF3333"
        elif float(sentiment) < 0.4:
            properties["color"] = "#FF9933"
        elif float(sentiment) < 0.6:
            properties["color"] = "#FFFF33"
        elif float(sentiment) < 0.8:
            properties["color"] = "#99FF33"
        else:
            properties["color"] = "#00BB00"

    with open('../static/map/res/melbourne_suburbs.geojson', 'w') as outFile:
        json.dump(geojson, outFile)
