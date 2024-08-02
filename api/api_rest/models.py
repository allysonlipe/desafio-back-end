from django.db import models

# Create your models here.

from django.db import models

class Pessoas(models.Model):
    id_pessoa = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    observacoes = models.TextField(blank=True, null=True)
    nome_mae = models.CharField(max_length=100, blank=True, null=True)
    nome_pai = models.CharField(max_length=100, blank=True, null=True)
    cpf = models.CharField(max_length=11, unique=True, blank=True, null=True)

    class Meta:
        indexes = [
            models.Index(fields=['nome']),
            models.Index(fields=['data_nascimento']),
        ]

    def __str__(self):
        return self.nome
