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
class Notificacao(models.Model):
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notificacoes')
    solicitacao = models.ForeignKey(Solicitacao, on_delete=models.CASCADE)
    mensagem = models.TextField(default="Mensagem padrão")
    lida = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notificação para {self.vendedor.username} sobre a solicitação de {self.solicitacao.produto.nome}"