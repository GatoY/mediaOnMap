from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('sentiment', views.sentiment, name='sentiment'),
    path('api/v1/sentimentData', views.sentimentData, name='sentimentData'),
    path('api/v1/sentiment_by_weekdays', views.sentiment_by_weekdays, name='sentiment_by_weekdays'),
    path('api/v1/sentiment_by_hours', views.sentiment_by_hours, name='sentiment_by_hours'),
    path('scenario1', views.scenario1, name='scenario1'),
    path('scenario2', views.scenario2, name='scenario2'),
    path('affordability', views.affordability, name='affordability'),
    path('api/v1/affordability_proportions', views.affordability_proportions, name='affordability_proportions'),
    path('aboutUs', views.aboutUs, name='aboutUs'),
    path('report', views.report, name='report'),
]
