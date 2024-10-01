from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from restaurantes.models import Restaurantes
from restaurantes.api.serializers import RestaurantesSerializers

# Create your views here.
@api_view(['GET'])
def Overview(request):
    urls = {
        'Find_By_Id':'restaurantes/list/<str:pk>',
        'List':'restaurantes/list/',
        'Create':'restaurantes/create/',
        'Update':'restaurantes/update/<str:pk>',
        'Delete':'restaurantes/delete/<str:pk>'
    }

    return Response(urls)

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
   
@api_view(['GET', 'POST'])
def Create(request):
    if request.method == 'GET':
        serializer = RestaurantesSerializers()
        return Response(serializer.data) 

    elif request.method == 'POST':
        serializer = RestaurantesSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'PUT'])
def Update(request, pk):
    if request.method == 'GET':
        serializer = RestaurantesSerializers()
        return Response(serializer.data) 
    elif request.method == 'POST':
        try:
            restaurante = Restaurantes.objects.get(id_restaurante=pk)
        except Restaurantes.DoesNotExist:
            return Response({'error': 'Restaurante não encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = RestaurantesSerializers(instance= restaurante, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Atualizado com Sucesso!'}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def Delete(request, pk):
    try:
        restaurante = Restaurantes.objects.get(id_restaurante=pk)
    except Restaurantes.DoesNotExist:
        return Response({'error': 'Restaurante não encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
    restaurante.delete()
    return Response({'message': 'Deletado com Sucesso'}, status=status.HTTP_200_OK)

            
