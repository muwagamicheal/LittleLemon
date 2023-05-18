#from django.shortcuts import render
from rest_framework import generics, status
from .models import MenuItem, ItemCategory
from .serializers import MenuItemSerializer, CategorySerializer

# 
from rest_framework.views import APIView
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
class MenuItemView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, IsManager)

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
     
    '''
    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    '''
# Used to manipulate individual items in menu-items in the database.
class MenuItemDetailView(APIView):
    permission_class = [permissions.IsAuthenticated, IsManager]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    #Retrieve Invidual Item
    def get_object(self, pk):
        try:
            return MenuItem.objects.get(id=pk)
        except MenuItem.DoesNotExist:
            return None
    #Retrieve individual item
    def get(self, request, pk, *arg, **kwargs):
        item = self.get_object(pk)
        if not item:
            return Response({"result":"Item Does not Exist"}, status=status.HTTP_400_BAD_REQUEST)
        result = MenuItemSerializer(item).data
        return Response(result, status=status.HTTP_200_OK)
    
    #Update Individual Item
    def put(self, request, pk,*args, **kwargs):
        update = self.get_object(pk)
        #item = generics.get_object_or_404(update, pk=pk)
        if not update:
            item = {'result','Item not found'}
            return Response(item, status=status.HTTP_404_BAD_REQUEST)
        data = {
            'item_name':request.data.get('item_name'),
            'description':request.data.get('description'),
            'price':request.data.get('price'),
            'item_category':request.data.get('item_category')
        }
        serializer = MenuItemSerializer(instance = update, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        #serializer = self.get_serializer(item, data=request.data)
        #serializer.is_valid(raise_exception=True)
        #serializer.save()
        return Response(serializer.errors, status=status.HTPP_400_BAD_REQUEST)
    
    #Delete Individual Item.
    def delete(self, request, pk, *args, **kwargs):
        item = self.get_object(pk)
        if not item:
            return Response({"response": "Object with Supplied ID does not exist"}, status=status.HTTP_400_BAD_REQUEST)
        item.delete()
        return Response({"response":"Item has been Deleted "},status=status.HTTP_200_OK)
        