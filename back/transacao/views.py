from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from transacao.models import Transacao
from transacao.api.serializers import TransacaoSerializer

# Create your views here.

@api_view(['GET'])
def Overview(request):
    urls = {
        'Find_By_Id':'transacoes/list/<str:pk>',
        'List':'transacoes/list/',
        'Create':'transacoes/create/',
        'Update':'transacoes/update/<str:pk>',
        'Delete':'transacoes/delete/<str:pk>'
    }

    return Response(urls)

@api_view(['GET'])
def List(request):

    transacoes = Transacao.objects.all()
    serializer = TransacaoSerializer(transacoes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def Find_By_Id(request, pk):
    try:
        transacao = Transacao.objects.get(id_transacao=pk)
    except Transacao.DoesNotExist:
        return Response({'error': 'Transação não encontrada'}, status=status.HTTP_404_NOT_FOUND)
    serializer = TransacaoSerializer(transacao, many=False)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def Create(request):
    if request.method == 'GET':
        serializer = TransacaoSerializer()
        return Response(serializer.data) 

    elif request.method == 'POST':
        serializer = TransacaoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT'])
def Update(request, pk):
    if request.method == 'GET':
        serializer = TransacaoSerializer()
        return Response(serializer.data) 
    elif request.method == 'POST':
        try:
            transacao = Transacao.objects.get(id_transacao=pk)
        except Transacao.DoesNotExist:
            return Response({'error': 'Trasação não encontrada'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = TransacaoSerializer(instance= transacao, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Atualizado com Sucesso!'}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def Delete(request, pk):
    try:
        transacao = Transacao.objects.get(id_transacao=pk)
    except Transacao.DoesNotExist:
        return Response({'error': 'Transação não encontrada'}, status=status.HTTP_404_NOT_FOUND)
    
    transacao.delete()
    return Response({'message': 'Deletado com Sucesso'}, status=status.HTTP_200_OK)