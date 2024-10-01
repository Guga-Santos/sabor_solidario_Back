from rest_framework import viewsets
from restaurantes.api import serializers
from restaurantes import models

class RestauranteViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RestaurantesSerializers
    queryset = models.Restaurantes.objects.all()