from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_mural, name='listar_mural'),
    #path('', views.home, name='home'),
]
