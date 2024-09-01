from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Solicitacao, Produto
from .forms import SolicitarProdutoForm

# ------- Método para listar todas as solicitações -------
@login_required
def listar_solicitacoes(request):
    solicitacoes = Solicitacao.objects.filter(comprador=request.user)
    return render(request, 'solicitacao/listar_solicitacoes.html', {'solicitacoes': solicitacoes})

# ------- Método para visualizar detalhes de uma solicitação -------
@login_required
def detalhar_solicitacao(request, id):
    solicitacao = get_object_or_404(Solicitacao, id=id)
    return render(request, 'solicitacao/detalhar_solicitacao.html', {'solicitacao': solicitacao})

# ------- Método para adicionar uma nova solicitação -------
@login_required
def adicionar_solicitacao(request):
    if request.method == 'POST':
        form = SolicitarProdutoForm(request.POST)
        produto_id = request.POST.get('produto_id')

        if not produto_id:
            return redirect('listar_produtos')  # Redireciona caso não tenha produto_id

        produto = get_object_or_404(Produto, id=produto_id)
        
        if form.is_valid():
            quantidade = form.cleaned_data['quantidade']
            solicitacao = Solicitacao.objects.create(
                comprador=request.user,
                produto=produto,
                vendedor=produto.usuario,
                quantidade=quantidade
            )
            # Criar notificação para o vendedor
            Notificacao.objects.create(
                vendedor=produto.usuario,
                solicitacao=solicitacao
            )
            return redirect('listar_solicitacoes')
    else:
        produto_id = request.GET.get('produto_id')
        if not produto_id:
            return redirect('listar_produtos')  # Redireciona caso não tenha produto_id
        
        produto = get_object_or_404(Produto, id=produto_id)
        form = SolicitarProdutoForm()
    
    return render(request, 'solicitacao/form_solicitacao.html', {'form': form, 'produto': produto})


# ------- Método para editar uma solicitação -------
@login_required
def editar_solicitacao(request, id):
    solicitacao = get_object_or_404(Solicitacao, id=id)
    if request.method == 'POST':
        form = SolicitarProdutoForm(request.POST, instance=solicitacao)
        if form.is_valid():
            form.save()
            return redirect('listar_solicitacoes')
    else:
        form = SolicitarProdutoForm(instance=solicitacao)
    return render(request, 'solicitacao/form_solicitacao.html', {'form': form})

# ------- Método para excluir uma solicitação -------
@login_required
def excluir_solicitacao(request, id):
    solicitacao = get_object_or_404(Solicitacao, id=id)
    if request.method == 'POST':
        solicitacao.delete()
        return redirect('listar_solicitacoes')
    return render(request, 'solicitacao/confirmar_exclusao.html', {'solicitacao': solicitacao})

@login_required
def listar_notificacoes(request):
    notificacoes = Notificacao.objects.filter(vendedor=request.user)
    return render(request, 'notificacao/listar_notificacoes.html', {'notificacoes': notificacoes})

@login_required
def responder_solicitacao(request, id, resposta):
    notificacao = get_object_or_404(Notificacao, id=id, vendedor=request.user)
    if resposta == 'aceitar':
        notificacao.aceita = True
    elif resposta == 'recusar':
        notificacao.aceita = False
    notificacao.lida = True
    notificacao.save()
    
    
    
    # Aqui você pode adicionar mais lógica, como enviar um email ao comprador
    return redirect('listar_notificacoes')
