from django.urls import path
from django.contrib import admin

from app.views import (
    home,
    form_cadastro_usuario,
    form_transacao,
    form_processo,
    form_projeto,
    view_usuarios,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="home"),
    path("form_cadastro_usuario/", form_cadastro_usuario, name="form_cadastro_usuario"),
    path("form_transacao/", form_transacao, name="form_transacao"),
    path("form_projeto/", form_projeto, name="form_projeto"),
    path("form_processo/", form_processo, name="form_processo"),
    path("view_usuarios/", view_usuarios, name="view_usuarios"),
]
