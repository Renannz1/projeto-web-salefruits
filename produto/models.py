from django.db import models
from django.contrib.auth.models import User

class Categoria(models.TextChoices):
    FRUTA = 'Fruta', 'Fruta'
    LEGUME = 'Legume', 'Legume'
    VERDURA = 'Verdura', 'Verdura'

class StatusProduto(models.TextChoices):
    PENDENTE = 'Pendente', 'Pendente'
    APROVADO = 'Aprovado', 'Aprovado'
    REJEITADO = 'Rejeitado', 'Rejeitado'

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='produtos')
    postado_em = models.DateTimeField(auto_now_add=True)
    quantidade = models.PositiveIntegerField(default=0) 
    categoria = models.CharField(max_length=10, choices=Categoria.choices, default=Categoria.FRUTA)  
    status = models.CharField(max_length=10, choices=StatusProduto.choices, default=StatusProduto.PENDENTE)
    imagem = models.ImageField(upload_to='produto/', null=True, blank=True)

    def __str__(self):
        return self.nome