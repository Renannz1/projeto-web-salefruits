from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Produto
from .forms import FiltroProdutoForm, ProdutoForm

def listar_produtos(request):
    form = FiltroProdutoForm(request.GET)
    
    # Obtém o usuário logado
    usuario = request.user
    
    # Filtra produtos apenas do usuário logado
    produtos = Produto.objects.filter(usuario=usuario)
    
    if form.is_valid():
        categoria = form.cleaned_data.get('categoria')
        if categoria:
            produtos = produtos.filter(categoria=categoria)
    
    return render(request, 'produto/listar_produtos.html', {'produtos': produtos, 'form': form})

@login_required
def adicionar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            produto = form.save(commit=False)
            produto.usuario = request.user  # Vincula o produto ao usuário logado
            produto.save()
            return redirect('listar_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'produto/form_produto.html', {'form': form})

@login_required
def editar_produto(request, id):
    produto = get_object_or_404(Produto, pk=id)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'produto/form_produto.html', {'form': form})

@login_required
def excluir_produto(request, id):
    produto = get_object_or_404(Produto, id=id, usuario=request.user)
    if request.method == 'POST':
        produto.delete()
        return redirect('listar_produtos')
    return render(request, 'produto/confirmar_exclusao.html', {'produto': produto})

@login_required
def detalhar_produto(request, id):
    # Obtém o produto com base no ID fornecido
    produto = get_object_or_404(Produto, id=id)
    # Renderiza o template 'detalhar_produto.html' com o contexto do produto
    return render(request, 'produtos/detalhar_produto.html', {'produto': produto})
