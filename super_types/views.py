from django.shortcuts import render
from django.shortcuts import render

# Create your views here.
from super_types.models import Super_Types
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from supers.models import Supers
from supers.serializers import SupersSerializer
from django.shortcuts import get_object_or_404


# Create your views here.

@api_view(['GET'])

def super_types_list(request):

    appending_dict_example = {}
    appending_dict_example['name'] = 'Bob'
    print(appending_dict_example)

    supers_type = Super_Types.objects.all()
    
    custom_response_dictionary = {}

    for super_types in super_types:

        supers = Supers.objects.filter(supers_id=supers.id)

        supers_serializer = SupersSerializer(supers, many=True)

        custom_response_dictionary[super_types.name] = {
            "address": super_types.address,
            "supers": supers_serializer.data
        }
    return Response(custom_response_dictionary)