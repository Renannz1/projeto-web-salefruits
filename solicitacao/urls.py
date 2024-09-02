from django.urls import path
from .views import aceitar_solicitacao, listar_notificacoes, listar_solicitacoes, detalhar_solicitacao, adicionar_solicitacao, editar_solicitacao, excluir_solicitacao, recusar_solicitacao

urlpatterns = [
    path('solicitacoes/', listar_solicitacoes, name='listar_solicitacoes'),
    path('solicitacao/<int:id>/', detalhar_solicitacao, name='detalhar_solicitacao'),
    path('solicitacao/adicionar/', adicionar_solicitacao, name='adicionar_solicitacao'),
    path('solicitacao/<int:id>/editar/', editar_solicitacao, name='editar_solicitacao'),
    path('solicitacao/<int:id>/excluir/', excluir_solicitacao, name='excluir_solicitacao'),
    path('notificacoes/', listar_notificacoes, name='listar_notificacoes'),
    path('aceitar-solicitacao/<int:notificacao_id>/', aceitar_solicitacao, name='aceitar_solicitacao'),
    path('recusar-solicitacao/<int:notificacao_id>/', recusar_solicitacao, name='recusar_solicitacao'),
]
