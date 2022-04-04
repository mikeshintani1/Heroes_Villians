from django.shortcuts import render

# Create your views here.
from super_types.models import Super_Types
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Supers
from .serializers import SupersSerializer
from django.shortcuts import get_object_or_404

# Create your views here.
@api_view(['GET','POST'])
def supers_list(request):
    if request.method == 'GET':
        supers = Supers.objects.all()
        serializer = SupersSerializer(supers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = SupersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def sort_heroes_list(request):

    super_types_param = request.query_params.get('super_types')
    sort_param = request.query_params.get('sort')

    supers = Supers.objects.all()

    if super_types_param:
        supers = supers.filter(super_types__type=super_types_param)

    if sort_param:
        supers = supers.order_by(sort_param)

    serializer = SupersSerializer(supers, many=True)
    return Response(serializer.data)
    
@api_view(['GET', 'PUT', 'DELETE'])
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
