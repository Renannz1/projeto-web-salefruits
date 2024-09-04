from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from chat.models import Room
from .models import Notificacao, Solicitacao, Produto
from .forms import SolicitarProdutoForm

#método para listar todas as solicitações
@login_required
def listar_solicitacoes(request):
    solicitacoes = Solicitacao.objects.filter(comprador=request.user)
    return render(request, 'solicitacao/listar_solicitacoes.html', {'solicitacoes': solicitacoes})

#método para visualizar detalhes de uma solicitação
@login_required
def detalhar_solicitacao(request, id):
    solicitacao = get_object_or_404(Solicitacao, id=id)
    return render(request, 'solicitacao/detalhar_solicitacao.html', {'solicitacao': solicitacao})

#método para adicionar uma nova solicitação
@login_required
def adicionar_solicitacao(request):
    if request.method == 'POST':
        form = SolicitarProdutoForm(request.POST)
        produto_id = request.POST.get('produto_id')

        if not produto_id:
            return redirect('listar_produtos')  #Redireciona caso não tenha produto_id

        produto = get_object_or_404(Produto, id=produto_id)
        
        if form.is_valid():
            quantidade = form.cleaned_data['quantidade']
            solicitacao = Solicitacao.objects.create(
                comprador=request.user,
                produto=produto,
                vendedor=produto.usuario,
                quantidade=quantidade
            )

            # Criar uma notificação para o vendedor
            Notificacao.objects.create(
                vendedor=produto.usuario,
                solicitacao=solicitacao,
                mensagem=f"{request.user.username} solicitou {quantidade} para o produto {produto.nome}."
                
            )
            return redirect('listar_solicitacoes')
    else:
        produto_id = request.GET.get('produto_id')
        if not produto_id:
            return redirect('listar_produtos')  # Redireciona caso não tenha produto_id
        
        produto = get_object_or_404(Produto, id=produto_id)
        form = SolicitarProdutoForm()
    
    return render(request, 'solicitacao/form_solicitacao.html', {'form': form, 'produto': produto})

#método para editar uma solicitação
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

#método para excluir uma solicitação
@login_required
def excluir_solicitacao(request, id):
    solicitacao = get_object_or_404(Solicitacao, id=id)
    if request.method == 'POST':
        solicitacao.delete()
        return redirect('listar_solicitacoes')
    return render(request, 'solicitacao/confirmar_exclusao.html', {'solicitacao': solicitacao})

#Lista todas as notificações não lidas do usuário logado e as exibe na página
@login_required
def listar_notificacoes(request):
    notificacoes = request.user.notificacoes.filter(lida=False)
    print("Notificações:", notificacoes)
    return render(request, 'listar_notificacoes.html', {'notificacoes': notificacoes})

#Permite ao vendedor aceitar uma solicitação. Atualiza o status da solicitação para "Aceita" e marca a notificação como lida.python
# Permite ao vendedor aceitar uma solicitação. Atualiza o status da solicitação para "Aceita" e marca a notificação como lida.
@login_required
def aceitar_solicitacao(request, notificacao_id):
    notificacao = get_object_or_404(Notificacao, id=notificacao_id)
    solicitacao = notificacao.solicitacao
    
    # Atualiza o status da solicitação para "Aceita" e marca a notificação como lida
    solicitacao.status = 'Aceita'
    solicitacao.save()
    notificacao.lida = True
    notificacao.save()
    
    # Cria a sala de chat
    room_title = f"Solicitação #{solicitacao.id}"
    room, created = Room.objects.get_or_create(
        title=room_title
    )
    
    if created:
        # Adiciona o comprador e o vendedor à sala
        room.users.add(solicitacao.comprador, solicitacao.vendedor)
    
    return redirect('home')



#Permite ao vendedor recusar uma solicitação. Atualiza o status da solicitação para "Recusada" e marca a notificação como lida.
@login_required
def recusar_solicitacao(request, notificacao_id):
    notificacao = get_object_or_404(Notificacao, id=notificacao_id)
    solicitacao = notificacao.solicitacao
    solicitacao.status = 'Recusada'
    solicitacao.save()
    notificacao.lida = True
    notificacao.save()
    return redirect('listar_notificacoes')
