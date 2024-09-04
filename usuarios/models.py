from django.contrib.auth.models import User
from django.db import models

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=255)
    descricao = models.TextField(blank=True)
    imagem_perfil = models.ImageField(upload_to='usuarios/', null=True, blank=True)  # Certifique-se de que este campo está definido

    def __str__(self):
        return self.nome
