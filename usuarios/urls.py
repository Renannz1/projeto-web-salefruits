from . import views
from django.urls import path
from .views import custom_logout, register, login_view


urlpatterns = [
    path('editar/<int:usuario_id>/', views.editar_usuario, name='editar_usuario'),
    path('excluir/<int:usuario_id>/', views.excluir_usuario, name='excluir_usuario'),

    path('perfil/', views.perfil_usuario, name='perfil_usuario'),

    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', custom_logout, name='logout'),
]