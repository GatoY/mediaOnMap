import json

with open('../static/map/res/affordability_slim.json') as f:
    data = json.load(f)
    result = {
        "rai_national_total_2017_q1": {"< 90": 0, "90 <= x < 110": 0, "110 <= x < 130": 0, "130 <= x < 150": 0,
                                       ">= 150": 0, "N/A": 0},
        "rai_national_total_2017_q2": {"< 90": 0, "90 <= x < 110": 0, "110 <= x < 130": 0, "130 <= x < 150": 0,
                                       ">= 150": 0, "N/A": 0},
        "rai_national_total_2016_q3": {"< 90": 0, "90 <= x < 110": 0, "110 <= x < 130": 0, "130 <= x < 150": 0,
                                       ">= 150": 0, "N/A": 0},
        "rai_national_total_2016_q4": {"< 90": 0, "90 <= x < 110": 0, "110 <= x < 130": 0, "130 <= x < 150": 0,
                                       ">= 150": 0, "N/A": 0}}

    for feature in data["features"]:
        if feature["properties"]["rai_national_total_2017_q1"] is None:
            result["rai_national_total_2017_q1"]["N/A"] += 1
        elif feature["properties"]["rai_national_total_2017_q1"] < 90:
            result["rai_national_total_2017_q1"]["< 90"] += 1
        elif 90 <= feature["properties"]["rai_national_total_2017_q1"] < 110:
            result["rai_national_total_2017_q1"]["90 <= x < 110"] += 1
        elif 110 <= feature["properties"]["rai_national_total_2017_q1"] < 130:
            result["rai_national_total_2017_q1"]["110 <= x < 130"] += 1
        elif 130 <= feature["properties"]["rai_national_total_2017_q1"] < 150:
            result["rai_national_total_2017_q1"]["130 <= x < 150"] += 1
        else:
            result["rai_national_total_2017_q1"][">= 150"] += 1

        if feature["properties"]["rai_national_total_2017_q2"] is None:
            result["rai_national_total_2017_q2"]["N/A"] += 1
        elif feature["properties"]["rai_national_total_2017_q2"] < 90:
            result["rai_national_total_2017_q2"]["< 90"] += 1
        elif 90 <= feature["properties"]["rai_national_total_2017_q2"] < 110:
            result["rai_national_total_2017_q2"]["90 <= x < 110"] += 1
        elif 110 <= feature["properties"]["rai_national_total_2017_q2"] < 130:
            result["rai_national_total_2017_q2"]["110 <= x < 130"] += 1
        elif 130 <= feature["properties"]["rai_national_total_2017_q2"] < 150:
            result["rai_national_total_2017_q2"]["130 <= x < 150"] += 1
        else:
            result["rai_national_total_2017_q2"][">= 150"] += 1

        if feature["properties"]["rai_national_total_2016_q3"] is None:
            result["rai_national_total_2016_q3"]["N/A"] += 1
        elif feature["properties"]["rai_national_total_2016_q3"] < 90:
            result["rai_national_total_2016_q3"]["< 90"] += 1
        elif 90 <= feature["properties"]["rai_national_total_2016_q3"] < 110:
            result["rai_national_total_2016_q3"]["90 <= x < 110"] += 1
        elif 110 <= feature["properties"]["rai_national_total_2016_q3"] < 130:
            result["rai_national_total_2016_q3"]["110 <= x < 130"] += 1
        elif 130 <= feature["properties"]["rai_national_total_2016_q3"] < 150:
            result["rai_national_total_2016_q3"]["130 <= x < 150"] += 1
        else:
            result["rai_national_total_2016_q3"][">= 150"] += 1

        if feature["properties"]["rai_national_total_2016_q4"] is None:
            result["rai_national_total_2016_q4"]["N/A"] += 1
        elif feature["properties"]["rai_national_total_2016_q4"] < 90:
            result["rai_national_total_2016_q4"]["< 90"] += 1
        elif 90 <= feature["properties"]["rai_national_total_2016_q4"] < 110:
            result["rai_national_total_2016_q4"]["90 <= x < 110"] += 1
        elif 110 <= feature["properties"]["rai_national_total_2016_q4"] < 130:
            result["rai_national_total_2016_q4"]["110 <= x < 130"] += 1
        elif 130 <= feature["properties"]["rai_national_total_2016_q4"] < 150:
            result["rai_national_total_2016_q4"]["130 <= x < 150"] += 1
        else:
            result["rai_national_total_2016_q4"][">= 150"] += 1

    with open('../static/map/res/affordability_proportions.json', 'w') as outFile:
        json.dump(result, outFile)

