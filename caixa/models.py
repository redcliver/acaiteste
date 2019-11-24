from django.db import models
from django.utils import timezone

# Create your models here.
class caixa_geral(models.Model):
    OP = (
        ('1', 'Entrada'),
        ('2', 'Saida'),
    )
    TP = (
        ('1', 'Dinheiro'),
        ('2', 'Cartao Debito'),
        ('3', 'Cartao Credito'),
        ('4', 'Boleto'),
        ('5', 'Transferencia'),
    )
    id = models.AutoField(primary_key=True)
    operacao = models.CharField(max_length=1, choices=OP, default=1)
    total = models.DecimalField(max_digits=10, decimal_places=2)    
    tipo = models.CharField(max_length=1, choices=TP, default=1)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    id_operacao = models.CharField(max_length=200)
    valor_operacao = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return str(self.id)