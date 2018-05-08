from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('sentiment', views.sentiment, name='sentiment'),
    path('avengers', views.avengers, name='avengers'),
    path('api/v1/avengers_data', views.avengers_data, name='avengers_data'),
    path('api/v1/sentiment_by_suburbs', views.sentiment_by_suburbs, name='sentiment_by_suburbs'),
    path('api/v1/sentiment_by_weekdays', views.sentiment_by_weekdays, name='sentiment_by_weekdays'),
    path('api/v1/sentiment_by_hours', views.sentiment_by_hours, name='sentiment_by_hours'),
    path('api/v1/word_cloud', views.word_cloud, name='word_cloud'),
    # path('scenario2', views.scenario2, name='scenario2'),
    path('traffic', views.traffic, name='traffic'),
    path('affordability', views.affordability, name='affordability'),
    path('api/v1/affordability_proportions', views.affordability_proportions, name='affordability_proportions'),
    path('aboutUs', views.aboutUs, name='aboutUs'),
    path('report', views.report, name='report'),
]
