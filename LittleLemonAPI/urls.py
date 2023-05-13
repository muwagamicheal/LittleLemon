#from django.contrib import admin
from django.urls import path
from . import views
#from django.conf.urls import url

## User registration andtoken generation endpoins
urlpatterns = [    
    path('menu-items/', views.MenuItemView.as_view(), name='menu_items'),
]