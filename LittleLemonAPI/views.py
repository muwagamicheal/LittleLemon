#from django.shortcuts import render
from rest_framework import generics
from .models import MenuItem, ItemCategory
from .serializers import MenuItemSerializer, CategorySerializer

# 
#from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
#from rest_framework import permissions

# Create your views here.

#Used to retrieve all categories in the database
class CategoryView(generics.ListCreateAPIView):
    queryset = ItemCategory.objects.all()
    serializer_class = CategorySerializer

 # Used to retrieve all menu items in the database
class MenuItemView(generics.ListCreateAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    ordering_fields = ['item_name','price']
    filtering_fields = ['price']
    search_fields = ['item_name']

     # Used to retrieve all menu items in the database
    def get(self, request):
        queryset = self.get_queryset()
        results = self.serializer_class(queryset, many=True).data    
        return Response(results)

     # Used to create new menu items in the database
    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data)       