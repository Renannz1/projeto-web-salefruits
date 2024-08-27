from django.shortcuts import render
from produto.models import Produto

def listar_mural(request):
    produtos = Produto.objects.all()  # Recupera todos os produtos
    return render(request, 'mural/listar_mural.html', {'produtos': produtos})
