from django.shortcuts import render
from produto.forms import FiltroProdutoForm
from produto.models import Produto



# Função para listar todos os produtos adicionados por todos os usuários
def listar_mural(request):
    # Inicializa o formulário de filtro com os dados de GET da requisição
    form = FiltroProdutoForm(request.GET)
    # Recupera todos os produtos do banco de dados
    produtos = Produto.objects.all()

    # Verifica se o formulário foi enviado e é válido
    if form.is_valid():
        # Recupera a categoria selecionada no formulário
        categoria = form.cleaned_data.get('categoria')
        if categoria:
            # Filtra os produtos pela categoria selecionada
            produtos = produtos.filter(categoria=categoria)

    # Renderiza o template de mural, passando a lista de produtos e o formulário
    return render(request, 'mural/listar_mural.html', {'produtos': produtos, 'form': form})


def home(request):
    return render(request, 'mural/listar_mural.html')
