from rest_framework import serializers
from .models import MenuItem, ItemCategory

# Serializer classes
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCategory
        fields = ['__all__']

class MenuItemSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(read_only=True)
    #item_category = CategorySerializer(write_only=True)
    class Meta:
        model = MenuItem
        fields = ['id','item_name','price','category_id','item_category',]

