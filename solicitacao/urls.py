from django.urls import path
from .views import listar_solicitacoes, detalhar_solicitacao, adicionar_solicitacao, editar_solicitacao, excluir_solicitacao

urlpatterns = [
    path('solicitacoes/', listar_solicitacoes, name='listar_solicitacoes'),
    path('solicitacao/<int:id>/', detalhar_solicitacao, name='detalhar_solicitacao'),
    path('solicitacao/adicionar/', adicionar_solicitacao, name='adicionar_solicitacao'),
    path('solicitacao/<int:id>/editar/', editar_solicitacao, name='editar_solicitacao'),
    path('solicitacao/<int:id>/excluir/', excluir_solicitacao, name='excluir_solicitacao'),
]
