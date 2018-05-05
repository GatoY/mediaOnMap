from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('sentiment', views.sentiment, name='sentiment'),
    path('scenario1', views.scenario1, name='scenario1'),
    path('scenario2', views.scenario2, name='scenario2'),
    path('scenario3', views.scenario3, name='scenario3'),
    path('aboutUs', views.aboutUs, name='aboutUs'),
    path('report', views.report, name='report'),
]
