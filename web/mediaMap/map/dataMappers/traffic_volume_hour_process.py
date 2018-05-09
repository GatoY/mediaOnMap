import json

with open('../static/map/img/trafficComplaintsByHours.json') as f:
    data = json.load(f)
    result = {}
    for row in data["rows"]:
        result[(int(row["key"]) + 10) % 24] = row["value"]

    with open('../static/map/res/traffic_by_hours.json', 'w') as outFile:
        json.dump(result, outFile)
