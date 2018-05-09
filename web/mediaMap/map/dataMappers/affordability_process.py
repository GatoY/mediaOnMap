import json

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
