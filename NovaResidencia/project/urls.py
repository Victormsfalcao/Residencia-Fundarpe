from django.urls import path
from django.contrib import admin

from app.views import (
    home,
    usuarios_html,
    transacao_html,
    projeto_html,
    processo_html,
    form_cadastro_usuario,
    form_transacao,
    form_processo,
    form_projeto,
    edit_usuario,
    edit_projeto,
    edit_processo,
    view_usuario,
    view_transacao,
    view_projeto,
    view_processo,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="home"),
    path("usuarios_html/", usuarios_html, name="usuarios_html"),
    path("transacao_html/", transacao_html, name="transacao_html"),
    path("projeto_html/", projeto_html, name="projeto_html"),
    path("processo_html/", processo_html, name="processo_html"),
    path("form_cadastro_usuario/", form_cadastro_usuario, name="form_cadastro_usuario"),
    path("form_transacao.html/", form_transacao, name="form_transacao"),
    path("form_projeto/", form_projeto, name="form_projeto"),
    path("form_processo/", form_processo, name="form_processo"),
    path("edit_usuario/<int:usuario_id>/", edit_usuario, name="edit_usuario"),
    path("edit_projeto/<int:projeto_id>/", edit_projeto, name="edit_projeto"),
    path("edit_processo/<int:processo_id>/", edit_processo, name="edit_processo"),
    path("view_usuario/<int:usuario_id>/", view_usuario, name="view_usuario"),
    path("view_transacao/<int:transacao_id>/", view_transacao, name="view_transacao"),
    path("view_projeto/<int:projeto_id>/", view_projeto, name="view_projeto"),
    path("view_processo/<int:processo_id>/", view_processo, name="view_processo"),
]
