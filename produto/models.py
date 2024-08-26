from django.db import models
from django.contrib.auth.models import User

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='produtos')
    postado_em = models.DateTimeField(auto_now_add=True)
    quantidade = models.PositiveIntegerField(default=0) 



    def __str__(self):
        return self.nome