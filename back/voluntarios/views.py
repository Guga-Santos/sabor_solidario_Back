from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from voluntarios.models import Voluntarios
from voluntarios.api.serializers import VoluntariosSerializer

# Create your views here.
@api_view(['GET'])
def Overview(request):
    urls = {
        'Find_By_Id':'voluntarios/list/<str:pk>',
        'List':'voluntarios/list/',
        'Create':'voluntarios/create/',
        'Update':'voluntarios/update/<str:pk>',
        'Delete':'voluntarios/delete/<str:pk>'
    }

    return Response(urls)

@api_view(['GET'])
def List(request):

    voluntarios = Voluntarios.objects.all()
    serializer = VoluntariosSerializer(voluntarios, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def Find_By_Id(request, pk):
    try:
        voluntario = Voluntarios.objects.get(id_voluntario=pk)
    except Voluntarios.DoesNotExist:
        return Response({'error': 'Voluntario não encontrado'}, status=status.HTTP_404_NOT_FOUND)
    serializer = VoluntariosSerializer(voluntario, many=False)
    return Response(serializer.data)
   
@api_view(['GET', 'POST'])
def Create(request):
    if request.method == 'GET':
        serializer = VoluntariosSerializer()
        return Response(serializer.data) 

    elif request.method == 'POST':
        serializer = VoluntariosSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT'])
def Update(request, pk):
    if request.method == 'GET':
        serializer = VoluntariosSerializer()
        return Response(serializer.data) 
    elif request.method == 'POST':
        try:
            voluntario = Voluntarios.objects.get(id_voluntario=pk)
        except Voluntarios.DoesNotExist:
            return Response({'error': 'Voluntario não encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = VoluntariosSerializer(instance= voluntario, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Atualizado com Sucesso!'}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def Delete(request, pk):
    try:
        voluntario = Voluntarios.objects.get(id_voluntario=pk)
    except Voluntarios.DoesNotExist:
        return Response({'error': 'Voluntario não encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
    voluntario.delete()
    return Response({'message': 'Deletado com Sucesso'}, status=status.HTTP_200_OK)

            
