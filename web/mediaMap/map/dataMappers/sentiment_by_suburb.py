import json

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
