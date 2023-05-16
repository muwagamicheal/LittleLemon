#from django.shortcuts import render
from rest_framework import generics, status
from .models import MenuItem, ItemCategory
from .serializers import MenuItemSerializer, CategorySerializer

# 
from rest_framework.views import APIView, View
from rest_framework.permissions import IsAuthenticated, BasePermissionMetaclass
from rest_framework.response import Response
from rest_framework import permissions

# Create your views here.
#View permissions using APIView

class BasePermission(metaclass=BasePermissionMetaclass):

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        return True

class IsManager(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False
        
        # Check if the user belongs to the "manager" group
        if request.user.groups.filter(name='manager').exists():
            return True
        
        return False

#Used to retrieve all categories in the database
class CategoryView(generics.ListCreateAPIView):
    queryset = ItemCategory.objects.all()
    serializer_class = CategorySerializer

 # Used to retrieve all menu items in the database
class MenuItemView(generics.ListCreateAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    permission_classes = (IsAuthenticated,IsManager)

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
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
# Used to manipulate individual items in menu-items in the database.
class MenuItemDetailView(APIView):
    permission_class = [IsAuthenticated]
    #queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    #Retrieve Invidual Item
    def get_object(self, pk):
           try:
               return MenuItem.objects.get(pk=pk)
           except MenuItem.DoesNotExist:
               #message = "Item not found"
               return Response( 'Item not found', status=status.HTTP_404_NOT_FOUND)
    def get(self, request, pk):
        item = self.get_object(pk)
        result = self.serializer_class(item, many=False)
        #item = generics.get_object_or_404(result, pk=pk)
        serializer = self.get_serializer(result)
        return Response(serializer.data)
    
    #Update Individual Item
    def put(self, request, pk):
        queryset = self.get_queryset()
        item = generics.get_object_or_404(queryset, pk=pk)
        
        serializer = self.get_serializer(item, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    #Delete Individual Item.
    def delete(self, request, pk):
        queryset = self.get_queryset()
        item = generics.get_object_or_404(queryset, pk=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        