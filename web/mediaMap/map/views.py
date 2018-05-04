from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
#from couchdb import Server
#from couchdb.client import ResourceNotFound

#SERVER = Server('http://127.0.0.1:5984')
#if(len(SERVER)==0):
#    SERVER.create()


def index(request):
    return render(request, 'map/index.html')


def map(request):
    return render(request,'map/chart.html')

def scenario1(request):
    return render(request,'map/scenario1.html')

def scenario2(request):
    return render(request,'map/scenario1.html')

def scenario3(request):
    return render(request,'map/scenario3.html')

def aboutUs(request):
    return render(request,'map/aboutUs.html')

def report(request):
    return render(request,'map/report.html')
# Create your views here.
