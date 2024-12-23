from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from uuid import uuid4
# Create your models here.

class Endereco(models.Model):
    rua = models.CharField(max_length=255)
    numero = models.CharField(max_length=10) 
    complemento = models.CharField(max_length=100, blank=True)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=8)

    def __str__(self):
        return f"{self.rua}, {self.numero}, {self.bairro}, {self.cidade}, {self.estado}, {self.cep}"


class Restaurantes(models.Model):
    id_restaurante = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    razao_social = models.CharField(max_length=255)
    nome_fantasia = models.CharField(max_length=255)
    CNPJ = models.CharField(max_length=14)
    telefone = models.CharField(max_length=11)
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE)
    email = models.EmailField()
    senha = models.CharField(max_length=128)

    def set_senha(self, raw_senha):
        self.senha = make_password(raw_senha)
    
    def verificar_senha(self, raw_senha):
        return check_password(raw_senha, self.senha)
    
    def __str__(self):
        return self.nome_fantasia