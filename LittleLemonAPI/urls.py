#from django.contrib import admin
from django.urls import path
from LittleLemonAPI import views
#from django.conf.urls import url

## User registration andtoken generation endpoins
urlpatterns = [    
    path('menu-items/', views.MenuItemView.as_view(), name='menu_items'),
    path('menu-items/<int:pk>',views.MenuItemDetailView.as_view(), name='item'),
]