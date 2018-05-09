import json

with open('../static/map/img/trafficVolumes.json') as f:
    data = json.load(f)
    for feature in data["features"]:
        volume = feature["properties"]["ALLVEHS_AADT"]
        if volume is None:
            feature["properties"]["color"] = "#666666"
        elif volume < 2000:
            feature["properties"]["color"] = "#00BB00"
        elif volume < 5000:
            feature["properties"]["color"] = "#99FF33"
        elif volume < 10000:
            feature["properties"]["color"] = "#FFD700"
        elif volume < 15000:
            feature["properties"]["color"] = "#FF9933"
        elif volume < 20000:
            feature["properties"]["color"] = "#FF3333"
        else:
            feature["properties"]["color"] = "#8B0000"

    with open('../static/map/res/traffic_volumes.geojson', 'w') as outFile:
        json.dump(data, outFile)
