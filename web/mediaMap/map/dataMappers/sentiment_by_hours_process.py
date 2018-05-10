import json

"""
====== COMP90024 TEAM 16 ======

889545   Yu Liu          yul22       yul22@student.unimelb.edu.au
875095   Jize Dong       jized       jized@student.unimelb.edu.au
911764   Minsheng Wang   minshengw   minshengw@student.unimelb.edu.au
890742   Minglun Zhang   minglunz    minglunz@student.unimelb.edu.au
905084   Xingping Ding   xingpingd   xingpingd@student.unimelb.edu.au

"""

with open('../static/map/img/sentimentByHours.json') as f:
    data = json.load(f)
    for row in data["rows"]:
        row["key"][0] = (int(row["key"][0]) + 10) % 24

    result = {
        0: {"positive": 0, "negative": 0, "neutral": 0},
        1: {"positive": 0, "negative": 0, "neutral": 0},
        2: {"positive": 0, "negative": 0, "neutral": 0},
        3: {"positive": 0, "negative": 0, "neutral": 0},
        4: {"positive": 0, "negative": 0, "neutral": 0},
        5: {"positive": 0, "negative": 0, "neutral": 0},
        6: {"positive": 0, "negative": 0, "neutral": 0},
        7: {"positive": 0, "negative": 0, "neutral": 0},
        8: {"positive": 0, "negative": 0, "neutral": 0},
        9: {"positive": 0, "negative": 0, "neutral": 0},
        10: {"positive": 0, "negative": 0, "neutral": 0},
        11: {"positive": 0, "negative": 0, "neutral": 0},
        12: {"positive": 0, "negative": 0, "neutral": 0},
        13: {"positive": 0, "negative": 0, "neutral": 0},
        14: {"positive": 0, "negative": 0, "neutral": 0},
        15: {"positive": 0, "negative": 0, "neutral": 0},
        16: {"positive": 0, "negative": 0, "neutral": 0},
        17: {"positive": 0, "negative": 0, "neutral": 0},
        18: {"positive": 0, "negative": 0, "neutral": 0},
        19: {"positive": 0, "negative": 0, "neutral": 0},
        20: {"positive": 0, "negative": 0, "neutral": 0},
        21: {"positive": 0, "negative": 0, "neutral": 0},
        22: {"positive": 0, "negative": 0, "neutral": 0},
        23: {"positive": 0, "negative": 0, "neutral": 0}
    }
    for entry in data["rows"]:
        result[entry["key"][0]][entry["key"][1]] += entry["value"]

    for key in result:
        percentage = result[key]["positive"] / (
                result[key]["positive"] + result[key]["negative"] + result[key]["neutral"])
        result[key]["percentage"] = round(percentage, 4)

    with open('../static/map/res/sentiment_by_hours.json', 'w') as outFile:
        json.dump(result, outFile)
