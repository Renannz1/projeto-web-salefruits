from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("usuarios/", include("usuarios.urls")),
    path('produtos/', include('produto.urls')), 
    path('mural/', include('mural.urls')),
]
