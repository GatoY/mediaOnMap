import os
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
import couchdb
import json
from django.http import HttpResponse


# from couchdb import Server
# from couchdb.client import ResourceNotFound

# server = couchdb.Server('http://root:Couchdbmima@127.0.0.1:5984')
# restResource = server['map']


def index(request):
    return render(request, 'map/index.html')


def sentiment(request):
    return render(request, 'map/sentiment.html')


# RESTful api
def sentiment_by_suburbs(request):
    with open('map/static/map/res/melbourne_suburbs.geojson') as f:
        data = json.load(f)
        return HttpResponse(json.dumps(data), content_type='application/json')


# RESTful api
def sentiment_by_hours(request):
    with open('map/static/map/res/sentiment_by_hours.json') as f:
        data = json.load(f)
        return HttpResponse(json.dumps(data), content_type='application/json')


# RESTful api
def sentiment_by_weekdays(request):
    with open('map/static/map/res/sentiment_by_weekdays.json') as f:
        data = json.load(f)
        return HttpResponse(json.dumps(data), content_type='application/json')


def word_cloud(request):
    with open('map/static/map/res/hot_topics_50.json') as f:
        data = json.load(f)
        return HttpResponse(json.dumps(data), content_type='application/json')


def avengers(request):
    return render(request, 'map/avengers.html')


def avengers_data(request):
    with open('map/static/map/res/avengers.json') as f:
        data = json.load(f)
        return HttpResponse(json.dumps(data), content_type='application/json')


# def scenario2(request):
#     return render(request, 'map/scenario2.html')
def traffic(request):
    return render(request, 'map/traffic.html')


def traffic_data(request):
    with open('map/static/map/res/traffic_volumes.geojson') as f:
        data = json.load(f)
        return HttpResponse(json.dumps(data), content_type='application/json')


def traffic_by_hours(request):
    with open('map/static/map/res/traffic_by_hours.json') as f:
        data = json.load(f)
        return HttpResponse(json.dumps(data), content_type='application/json')


def affordability(request):
    return render(request, 'map/affordability.html')


def affordability_proportions(request):
    with open('map/static/map/res/affordability_proportions.json') as f:
        data = json.load(f)
        return HttpResponse(json.dumps(data), content_type='application/json')


def aboutUs(request):
    return render(request, 'map/aboutUs.html')


def report(request):
    return render(request, 'map/report.html')
