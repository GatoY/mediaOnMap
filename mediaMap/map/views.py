from django.shortcuts import render


def index(request):
    return render(request, 'map/index.html')


def map(request):
    return render(request, 'map/chart.html')
# Create your views here.
