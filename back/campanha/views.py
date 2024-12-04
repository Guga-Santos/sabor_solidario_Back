from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from campanha.models import Campanha
from campanha.api.serializers import CampanhaSerializer

# Create your views here.

@api_view(['GET'])
def Overview(request):
    urls = {
        'Find_By_Id':'campanhas/list/<str:pk>',
        'List':'campanhas/list/',
        'Create':'campanhas/create/',
        'Update':'campanhas/update/<str:pk>',
        'Delete':'campanhas/delete/<str:pk>'
    }

    return Response(urls)

@api_view(['GET'])
def List(request):

    campanhas = Campanha.objects.all()
    serializer = CampanhaSerializer(campanhas, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def Find_By_Id(request, pk):
    try:
        campanha = Campanha.objects.get(id_campanha=pk)
    except Campanha.DoesNotExist:
        return Response({'error': 'Campanha não encontrada'}, status=status.HTTP_404_NOT_FOUND)
    serializer = CampanhaSerializer(campanha, many=False)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def Create(request):
    if request.method == 'GET':
        serializer = CampanhaSerializer()
        return Response(serializer.data) 

    elif request.method == 'POST':
        serializer = CampanhaSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT'])
def Update(request, pk):
    if request.method == 'GET':
        serializer = CampanhaSerializer()
        return Response(serializer.data) 
    elif request.method == 'PUT':
        try:
            campanha = Campanha.objects.get(id_campanha=pk)
            serializer = CampanhaSerializer(instance=campanha, data=request.data, partial=True)
        except Campanha.DoesNotExist:
            return Response({'error': 'Campanha não encontrada'}, status=status.HTTP_404_NOT_FOUND)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Atualizado com Sucesso!'}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def Delete(request, pk):
    try:
        campanha = Campanha.objects.get(id_campanha=pk)
        campanha.delete()
        return Response({'message': 'Deletado com Sucesso'}, status=status.HTTP_200_OK)
    except Campanha.DoesNotExist:
        return Response({'error': 'Campanha não encontrada'}, status=status.HTTP_404_NOT_FOUND)
    
