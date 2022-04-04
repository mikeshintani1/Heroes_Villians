from rest_framework import serializers
from .models import Supers

class SupersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supers
        fields = ['id', 'name', 'alter_ego', 'primary_ability', 'secondary_ability', 'catchphrase', 'super_types']
        depth = 1
    
    super_types_id = serializers.IntegerField(write_only=True)