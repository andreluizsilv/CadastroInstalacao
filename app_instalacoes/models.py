from django.db import models
from decimal import Decimal
from django.utils import timezone

class Instalacao(models.Model):
    id_instalacoes = models.AutoField(primary_key=True)
    pedido = models.CharField(max_length=20)
    vendedor = models.TextField(max_length=100)
    metragem = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    data_criacao = models.DateField(default=timezone.now)

    def __str__(self):
        return self.pedido
