from webbrowser import get
from django.shortcuts import render
from rest_framework import filters
# Create your views here.
# from super_types.models import Super_Types
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Supers
from .serializers import SupersSerializer
from django.shortcuts import get_object_or_404
from super_types.models import Super_Types
from super_types.models import Power
# Create your views here.

@api_view(['GET','POST'])
def supers_list(request):
    supers = Supers.objects.all()
    super_types_param = request.query_params.get('type')
    sort_param = request.query_params.get('sort')
    custom_response_dictionary = {}
    if super_types_param:
        supers = supers.filter(super_types__type = super_types_param)
        serializer = SupersSerializer(supers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif sort_param:
        supers = supers.order_by(sort_param)
        serializer = SupersSerializer(supers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
     
    if request.method == 'GET':
        super_types = Super_Types.objects.all()
    
        for super_types in super_types:
        
            supers = Supers.objects.filter(super_types=super_types)
            supers_serializer = SupersSerializer(supers, many=True)
            custom_response_dictionary[super_types.type] = {
                "types": super_types.type,
                "supers": supers_serializer.data
            }
            # return Response(serializer.data, status=status.HTTP_200_OK) 
        return Response(custom_response_dictionary)
  
    if request.method == 'POST':
        serializer = SupersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def supers_detail(request, pk):
    supers = get_object_or_404(Supers, pk=pk)
    if request.method == 'GET':
        serializer = SupersSerializer(supers)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = SupersSerializer(supers, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        supers.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['PATCH'])
def power_ability(request, id, pk):
    supers = get_object_or_404(Supers, pk=pk)
    power = get_object_or_404(Power, id=id)
    update_super = supers.power_ability.add(power)
    serializer = SupersSerializer(update_super)

    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)