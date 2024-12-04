from rest_framework import serializers
from campanha.models import Campanha

class CampanhaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campanha
        fields = ['id_campanha', 'restaurante', 'titulo', 'descricao', 'data_inicio', 'data_fim', 'horario', 'tipo', 'disponivel']
