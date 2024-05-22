from django.urls import path

from app.views import (
    home,
    form_cadastro_usuario,
    form_transacao,
    form_processo,
    form_projeto,
)

urlpatterns = [
    path("", home, name="home"),
    path("form_cadastro_usuario/", form_cadastro_usuario, name="form_cadastro_usuario"),
    path("form_transacao/", form_transacao, name="form_transacao"),
    path("form_projeto/", form_projeto, name="form_projeto"),
    path("form_processo/", form_processo, name="form_processo"),
]
