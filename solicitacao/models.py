from django.db import models
from django.contrib.auth.models import User
from produto.models import Produto

class Solicitacao(models.Model):
    comprador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='solicitacoes_feitas')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='solicitacoes_recebidas')
    quantidade = models.PositiveIntegerField()
    data_solicitacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.comprador.username} solicitou {self.quantidade} de {self.produto.nome}"
