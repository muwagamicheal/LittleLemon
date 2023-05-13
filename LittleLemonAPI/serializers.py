from rest_framework import serializers
from .models import MenuItem

# Serializer classes

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id','item_name','price']