from django.shortcuts import render

# Create your views here.
# from super_types.models import Super_Types
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Supers
from .serializers import SupersSerializer
from django.shortcuts import get_object_or_404

# Create your views here.

@api_view(['GET','POST'])
def supers_list(request):
    super_types_param = request.query_params.get('type')
    sort_param = request.query_params.get('sort')
    supers = Supers.objects.all()
    if request.method == 'GET':
        super_types_param
    elif super_types_param:
        supers = supers.filter(Super_Types_type=super_types_param)
    elif sort_param:
        supers = supers.order_by(sort_param)
        serializer = SupersSerializer(supers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = SupersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['GET'])
# def sort_heroes_list(request):

#     super_types_param = request.query_params.get('type')
#     sort_param = request.query_params.get('sort')
#     supers = Supers.objects.all()


#     serializer = SupersSerializer(supers, many=True)
#     return Response(serializer.data)
    
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

# @api_view(['GET'])

# def review_list(request):

#     # appending_dict_example = {}
#     # appending_dict_example['type'] = 'villian'
#     # print(appending_dict_example)

#     super_types = Super_Types.objects.all()
    
#     custom_response_dictionary = {}

#     for super_types in super_types:

#         supers = Supers.objects.filter(supers_id=supers.id)

#         supers_serializer = SupersSerializer(supers, many=True)

#         custom_response_dictionary[super_types.type] = {
#             "type": super_types.type,
#             "id": supers_serializer.id
#         }
#         return Response(custom_response_dictionary)