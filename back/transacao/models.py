from datetime import timezone
from django.db import models
from uuid import uuid4
from campanha.models import Campanha
from voluntarios.models import Voluntarios

class Transacao(models.Model):
    id_transacao = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    campanha = models.ForeignKey(Campanha, on_delete=models.CASCADE, related_name="transacoes")
    voluntario = models.ForeignKey(Voluntarios, on_delete=models.CASCADE, related_name="transacoes")
    data_reserva = models.DateTimeField(auto_now_add=True)  # Quando o voluntário se inscreveu
    data_retirada = models.DateTimeField(null=True, blank=True)  # Quando o alimento foi retirado
    status = models.CharField(
        max_length=20,
        choices=[('Pendente', 'Pendente'), ('Concluida', 'Concluída')],
        default='Pendente'
    )

    def finalizar_retirada(self):
        """Marca a transação como concluída"""
        self.status = 'Concluida'
        self.data_retirada = timezone.now()
        self.save()

    def __str__(self):
        return f"Transação {self.id_transacao} - {self.campanha.titulo}"
