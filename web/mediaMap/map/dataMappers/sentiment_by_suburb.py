import json

with open('../static/map/img/ToMason.json') as f:
    data = json.load(f)

    result = {}
    for entry in data["rows"]:
        if entry["key"] is not None:
            if entry["key"][1] not in result.keys():
                result[entry["key"][1]] = {"suburb_name": entry["key"][0], "positive": 0, "negative": 0, "neutral": 0}
            result[entry["key"][1]][entry["key"][2]] = entry["value"]

    for key in result:
        percentage = result[key]["positive"] / (
                result[key]["positive"] + result[key]["negative"] + result[key]["neutral"])
        result[key]["score"] = round(percentage, 4)

    print(result)

    with open('../static/map/res/affordability20162017.geojson') as g:
        geojson = json.load(g)
        for feature in geojson["features"]:
            feature["properties"].pop("rai_national_total_2017_q1")
            feature["properties"].pop("rai_national_total_2017_q2")
            feature["properties"].pop("rai_national_total_2016_q3")
            feature["properties"].pop("rai_national_total_2016_q4")
            code = feature["properties"]["geography_name"]
            if code in result.keys():
                feature["properties"]["suburb_name"] = result[code]["suburb_name"]
                feature["properties"]["positive"] = result[code]["positive"]
                feature["properties"]["negative"] = result[code]["negative"]
                feature["properties"]["neutral"] = result[code]["neutral"]
                feature["properties"]["score"] = result[code]["score"]
                sentiment = result[code]["score"]
                if sentiment < 0.2:
                    feature["properties"]["color"] = "#FF3333"
                elif sentiment < 0.4:
                    feature["properties"]["color"] = "#FF9933"
                elif sentiment < 0.6:
                    feature["properties"]["color"] = "#FFFF33"
                elif sentiment < 0.8:
                    feature["properties"]["color"] = "#99FF33"
                else:
                    feature["properties"]["color"] = "#00BB00"
            else:
                feature["properties"]["color"] = "#666666"

        with open('../static/map/res/melbourne_suburbs.geojson', 'w') as outFile:
            json.dump(geojson, outFile)
