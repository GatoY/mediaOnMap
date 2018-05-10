import json

"""
====== COMP90024 TEAM 16 ======

889545   Yu Liu          yul22       yul22@student.unimelb.edu.au
875095   Jize Dong       jized       jized@student.unimelb.edu.au
911764   Minsheng Wang   minshengw   minshengw@student.unimelb.edu.au
890742   Minglun Zhang   minglunz    minglunz@student.unimelb.edu.au
905084   Xingping Ding   xingpingd   xingpingd@student.unimelb.edu.au

"""

with open('../static/map/img/sentimentByWeekdays.json') as f:
    data = json.load(f)
    result = {"Mon": {"positive": 0, "negative": 0, "neutral": 0},
              "Tue": {"positive": 0, "negative": 0, "neutral": 0},
              "Wed": {"positive": 0, "negative": 0, "neutral": 0},
              "Thu": {"positive": 0, "negative": 0, "neutral": 0},
              "Fri": {"positive": 0, "negative": 0, "neutral": 0},
              "Sat": {"positive": 0, "negative": 0, "neutral": 0},
              "Sun": {"positive": 0, "negative": 0, "neutral": 0}}

    entries = data["rows"]
    for entry in entries:
        result[entry["key"][0]][entry["key"][1]] += entry["value"]

    for key in result:
        percentage = result[key]["positive"] / (
                result[key]["positive"] + result[key]["negative"] + result[key]["neutral"])
        result[key]["percentage"] = round(percentage, 4)

    with open('../static/map/res/sentiment_by_weekdays.json', 'w') as outFile:
        json.dump(result, outFile)
