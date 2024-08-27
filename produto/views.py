from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Produto
from .forms import FiltroProdutoForm, ProdutoForm



# ------- metodo para listar produtos -------
@login_required
def listar_produtos(request):
    # Obtém o resultado do formulário de filtro de produto
    form = FiltroProdutoForm(request.GET)
    # Obtém o usuário logado
    usuario = request.user  
    # Filtra produtos apenas do usuário logado
    produtos = Produto.objects.filter(usuario=usuario)
    
    # Verifica se o formulário foi enviado corretamente
    if form.is_valid():
        # E então recupera a categoria selecionada no formulário usando form.cleaned_data.get('categoria')
        categoria = form.cleaned_data.get('categoria')
        if categoria:
            produtos = produtos.filter(categoria=categoria)
    
    return render(request, 'produto/listar_produtos.html', {'produtos': produtos, 'form': form})




# ------- metodo para adicionar um novo produto que sera vinculado ao usuario que está logado -------
@login_required
def adicionar_produto(request):
    # Verifica se o método da requisição é POST (submissão de formulário)
    if request.method == 'POST':
        # Cria uma instância do formulário com os dados enviados
        form = ProdutoForm(request.POST)

        # Verifica se o formulário é válido
        if form.is_valid():
            # Cria um objeto produto, mas ainda não o salva no banco de dados
            produto = form.save(commit=False)
            # Vincula o produto ao usuário logado
            produto.usuario = request.user  
            # Salva o produto no banco de dados
            produto.save()
            # Redireciona para a lista de produtos
            return redirect('listar_produtos')
    else:
        # Se a requisição não for POST, exibe um formulário em branco
        form = ProdutoForm()

    # Renderiza o template com o formulário de produto
    return render(request, 'produto/form_produto.html', {'form': form})




# ------- metodo para editar o produto -------
@login_required
def editar_produto(request, id):
    # Tenta obter o produto pelo id, ou retorna 404 se não encontrado
    produto = get_object_or_404(Produto, pk=id)

    # Verifica se o método da requisição é POST (submissão de formulário)
    if request.method == 'POST':
        # Cria uma instância do formulário com os dados enviados e associa ao produto existente
        form = ProdutoForm(request.POST, instance=produto)
        # Verifica se o formulário é válido
        if form.is_valid():
            # Salva as mudanças no produto
            form.save()
            # Redireciona para a lista de produtos
            return redirect('listar_produtos')
    else:
        # Se a requisição não for POST, preenche o formulário com os dados do produto existente
        form = ProdutoForm(instance=produto)
        
    # Renderiza o template com o formulário de produto
    return render(request, 'produto/form_produto.html', {'form': form})




# ------- metodo para  excluir um produto existente -------
@login_required
def excluir_produto(request, id):
    # Tenta obter o produto pelo id e usuário logado, ou retorna 404 se não encontrado
    produto = get_object_or_404(Produto, id=id, usuario=request.user)
    # Verifica se o método da requisição é POST (confirmação de exclusão)
    if request.method == 'POST':
        # Exclui o produto do banco de dados
        produto.delete()
        # Redireciona para a lista de produtos
        return redirect('listar_produtos')
    # Renderiza o template de confirmação de exclusão com o produto
    return render(request, 'produto/confirmar_exclusao.html', {'produto': produto})




# ------- metodo para visualizar todas as informações de um produto -------
@login_required
def detalhar_produto(request, id):
    # Obtém o produto com base no ID fornecido
    produto = get_object_or_404(Produto, id=id)
    # Renderiza o template 'detalhar_produto.html' com o contexto do produto
    return render(request, 'produtos/detalhar_produto.html', {'produto': produto})
