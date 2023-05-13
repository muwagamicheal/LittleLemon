#from django.shortcuts import render
from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerializer

# 
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
#from rest_framework import permissions

# Create your views here.

 # Used to retrieve all menu items in the database
class MenuItemView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    ordering_fields = ['item_name','price']
    filtering_fields = ['price']
    search_fields = ['item_name']
"""
    def get(self, request):
        if self.has_permission(request, self):
            queryset = self.get_queryset()
            results = self.serializer_class(queryset, many=True).data
            
            return Response(results)
        else:
            # Do something else if user does not have permission
            return Response('User does not have permission')
"""