from rest_framework import viewsets
from campanha.api import serializers
from campanha import models

class CampanhaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CampanhaSerializer
    queryset = models.Campanha.objects.all()