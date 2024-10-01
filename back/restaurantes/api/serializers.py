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
        fields = ['id_restaurante', 'nome', 'nome_fantasia', 'CNPJ', 'telefone', 'email', 'senha', 'endereco']  # Inclua "endereco" nos fields

    def create(self, validated_data):
        # Extrair os dados do endereço
        endereco_data = validated_data.pop('endereco')
        # Criar o objeto endereço primeiro
        endereco = Endereco.objects.create(**endereco_data)
        # Criar o objeto restaurante com o endereço
        restaurante = Restaurantes.objects.create(endereco=endereco, **validated_data)
        return restaurante

    def update(self, instance, validated_data):
        # Atualizar os dados do endereço
        endereco_data = validated_data.pop('endereco')
        endereco = instance.endereco

        # Atualiza os campos do endereço
        for attr, value in endereco_data.items():
            setattr(endereco, attr, value)
        endereco.save()

        # Atualizar os outros campos do restaurante
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance
