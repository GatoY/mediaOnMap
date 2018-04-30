from django.urls import path,include

urlpatterns = [
               path('map/', include('map.urls')),
               ]
