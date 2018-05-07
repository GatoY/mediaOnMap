import os
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
import couchdb
import json
from django.http import HttpResponse

# from couchdb import Server
# from couchdb.client import ResourceNotFound

server = couchdb.Server('http://admin:admin@127.0.0.1:5984')
restResource = server['test']


def index(request):
    return render(request, 'map/index.html')


def sentiment(request):
    return render(request, 'map/sentiment.html')


def sentimentData(request):
    sentiment_data = restResource["f331f3a656450464d3c8c9cbb800c5b1"]
    return HttpResponse(json.dumps(sentiment_data), content_type='application/json')


def sentiment_by_weekdays(request):
    with open('map/static/map/res/sentiment_by_weekdays.json') as f:
        data = json.load(f)
        for key in data:
            data[key]["percentage"] = data[key]["positive"] / (
                        data[key]["positive"] + data[key]["negative"] + data[key]["neutral"])
        return HttpResponse(json.dumps(data), content_type='application/json')


def scenario1(request):
    return render(request, 'map/scenario1.html')


def scenario2(request):
    return render(request, 'map/scenario2.html')


def affordability(request):
    return render(request, 'map/affordability.html')


def affordability_proportions(request):
    with open('map/static/map/res/affordability_slim.json') as f:
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

        return HttpResponse(json.dumps(result), content_type='application/json')


def aboutUs(request):
    return render(request, 'map/aboutUs.html')


def report(request):
    return render(request, 'map/report.html')
# Create your views here.
