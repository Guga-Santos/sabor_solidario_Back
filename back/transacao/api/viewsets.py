from rest_framework import viewsets
from transacao.api import serializers
from transacao import models

class TransacaoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TransacaoSerializer
    queryset = models.Transacao.objects.all()