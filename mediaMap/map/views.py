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
# Create your views here.
