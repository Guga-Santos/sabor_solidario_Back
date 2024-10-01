from rest_framework import serializers
from restaurantes import models

class RestaurantesSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Restaurantes
        fields = '__all__'