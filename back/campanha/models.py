from django.db import models
from restaurantes.models import Restaurantes
from uuid import uuid4

# Create your models here.

class Campanha(models.Model):
    id_campanha = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    restaurante = models.ForeignKey(Restaurantes, on_delete=models.CASCADE, related_name="campanhas")
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_fim = models.DateField()
    horario = models.CharField(max_length=8)
    tipo = models.CharField(max_length=64)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.titulo} - {self.restaurante.nome_fantasia}"