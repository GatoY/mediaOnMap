import json

with open('../static/map/img/melbourne_suburb.geojson') as f:
    geojson = json.load(f)

    for feature in geojson["features"]:
        sentiment = feature["properties"]["pos_rate"]

        if sentiment is None:
            feature["properties"]["color"] = "#666666"
        elif float(sentiment) < 0.2:
            feature["properties"]["color"] = "#FF3333"
        elif float(sentiment) < 0.4:
            feature["properties"]["color"] = "#FF9933"
        elif float(sentiment) < 0.6:
            feature["properties"]["color"] = "#FFFF33"
        elif float(sentiment) < 0.8:
            feature["properties"]["color"] = "#99FF33"
        else:
            feature["properties"]["color"] = "#00BB00"

    with open('../static/map/res/melbourne_suburbs.geojson', 'w') as outFile:
        json.dump(geojson, outFile)
