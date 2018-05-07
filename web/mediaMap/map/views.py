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


def scenario1(request):
    return render(request, 'map/scenario1.html')


def scenario2(request):
    return render(request, 'map/scenario2.html')


def scenario3(request):
    return render(request, 'map/scenario3.html')


def aboutUs(request):
    return render(request, 'map/aboutUs.html')


def report(request):
    return render(request, 'map/report.html')
# Create your views here.
