from rest_framework import serializers
from restaurantes.models import Restaurantes, Endereco

# Serializer para o Endereço
class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ['rua', 'numero', 'complemento', 'bairro', 'cidade', 'estado', 'cep']

# Serializer para o Restaurante
class RestaurantesSerializers(serializers.ModelSerializer):
    endereco = EnderecoSerializer()  # Isso garante que o campo "endereco" seja exibido corretamente
    senha = serializers.CharField(write_only=True)

    class Meta:
        model = Restaurantes
        fields = ['id_restaurante', 'razao_social', 'nome_fantasia', 'CNPJ', 'telefone', 'email', 'senha', 'endereco']

    def create(self, validated_data):
        endereco_data = validated_data.pop('endereco', None)
        
        if not endereco_data:
            raise serializers.ValidationError({"endereco": "O campo endereço é obrigatório."})
        
        # Criar o objeto endereço primeiro
        endereco_serializer = EnderecoSerializer(data=endereco_data)
        endereco_serializer.is_valid(raise_exception=True)
        endereco = endereco_serializer.save()

        # Criar o objeto restaurante com o endereço
        restaurante = Restaurantes.objects.create(endereco=endereco, **validated_data)
        return restaurante

    def update(self, instance, validated_data):
        # Atualizar os dados do endereço
        endereco_data = validated_data.pop('endereco', None)
        endereco = instance.endereco

        if endereco_data:
            endereco_serializer = EnderecoSerializer(instance=endereco, data=endereco_data)
            endereco_serializer.is_valid(raise_exception=True)
            endereco_serializer.save()

        # Atualizar os outros campos do restaurante
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance
