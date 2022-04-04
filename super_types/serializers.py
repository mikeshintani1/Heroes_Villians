from rest_framework import serializers
from .models import Super_Types

class Super_TypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Super_Types
        fields = ['id', 'name', 'super_type']