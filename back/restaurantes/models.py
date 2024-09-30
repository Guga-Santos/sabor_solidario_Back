from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from uuid import uuid4
# Create your models here.

class Restaurantes(models.Model):
    id_restaurante = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=255)
    nome_fantasia = models.CharField(max_length=255)
    CNJP = models.CharField(max_length=14)
    telefone = models.CharField(max_length=11)
    email = models.EmailField()
    senha = models.CharField(max_length=128)

    def set_senha(self, raw_senha):
        self.senha = make_password(raw_senha)
    
    def verificar_senha(self, raw_senha):
        return check_password(raw_senha, self.senha)
    
    def __str__(self):
        return self.nome