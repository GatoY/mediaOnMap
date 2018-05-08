from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/v1/sentiment', views.sentiment),

    path('index', views.index, name='index'),
    path('sentiment', views.sentiment, name='sentiment'),
    path('sentimentData', views.sentimentData, name='sentimentData'),
    path('sentiment_by_weekdays', views.sentiment_by_weekdays, name='sentiment_by_weekdays'),
    path('sentiment_by_hours', views.sentiment_by_hours, name='sentiment_by_hours'),
    # path('scenario1', views.scenario1, name='scenario1'),
    path('avengers', views.avengers, name='avengers'),
    path('scenario2', views.scenario2, name='scenario2'),
    path('affordability', views.affordability, name='affordability'),
    path('affordability_proportions', views.affordability_proportions, name='affordability_proportions'),
    path('aboutUs', views.aboutUs, name='aboutUs'),
    path('report', views.report, name='report'),
]
