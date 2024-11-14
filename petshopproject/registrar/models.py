from django.db import models

class Registrar(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True, default=None)
    data = models.DateTimeField()
    concluido = models.BooleanField(default=False)
# Create your models here.
