from rest_framework import serializers
from voluntarios.models import Voluntarios, Endereco

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'

class VoluntariosSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer()
    senha = serializers.CharField(write_only=True)

    class Meta:
        model = Voluntarios
        fields = ['id_voluntario', 'nome', 'CPF', 'telefone', 'grupo', 'email', 'senha', 'endereco']

    def create(self, validated_data):
        # Extrair os dados do endereço
        endereco_data = validated_data.pop('endereco')
        # Criar o objeto endereço primeiro
        endereco = Endereco.objects.create(**endereco_data)
        # Criar o objeto restaurante com o endereço
        restaurante = Voluntarios.objects.create(endereco=endereco, **validated_data)
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
