from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from restaurantes.models import Restaurantes
from restaurantes.api.serializers import RestaurantesSerializers

# Create your views here.

@api_view(['GET'])
def List(request):

    restaurantes = Restaurantes.objects.all()
    serializer = RestaurantesSerializers(restaurantes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def Find_By_Id(request, pk):
    try:
        restaurante = Restaurantes.objects.get(id_restaurante=pk)
    except Restaurantes.DoesNotExist:
        return Response({'error': 'Restaurante não encontrado'}, status=status.HTTP_404_NOT_FOUND)
    serializer = RestaurantesSerializers(restaurante, many=False)
    return Response(serializer.data)
   
   
   
   
   
   
   
    # url_list = {
    #     "List": "/restaurantes",
    #     "FindByID": "/restaurantes/<str:pk>/",
    #     "Create": "restaurantes",
    #     "Update": "restaurantes/<str:pk>/",
    #     "Delete": "restaurantes/<str:pk>/"
    # }
    # return Response(url_list)
