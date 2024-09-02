from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.listar_produtos, name='listar_produtos'),
    path('adicionar/', views.adicionar_produto, name='adicionar_produto'),
    path('editar/<int:id>/', views.editar_produto, name='editar_produto'),
    path('excluir/<int:id>/', views.excluir_produto, name='excluir_produto'),
    path('detalhes/<int:id>/', views.detalhar_produto, name='detalhar_produto'),
    path('aprovar/', views.aprovar_produtos, name='aprovar_produtos'),  

]
