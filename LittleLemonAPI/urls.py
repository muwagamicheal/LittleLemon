#from django.contrib import admin
from django.urls import path, include
#from django.conf.urls import url

## User registration andtoken generation endpoins
urlpatterns = [    
    path('users', include('djoser.urls')),
]