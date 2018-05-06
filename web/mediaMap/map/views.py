from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
import couchdb

# from couchdb import Server
# from couchdb.client import ResourceNotFound

server = couchdb.Server('http://root:Couchdbmima@127.0.0.1:5984')


def index(request):
    return render(request, 'map/index.html')


def sentiment(request):
    return render(request, 'map/sentiment.html')

def sentiment(request):


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
