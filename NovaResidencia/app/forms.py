from django import forms
from .models import CadastroUsuario, Transacao, Projeto, Processo


class CadastroUsuarioForm(forms.ModelForm):
    class Meta:
        model = CadastroUsuario
        fields = ["nome", "email", "senha", "setor"]


class TransacaoForm(forms.ModelForm):
    usuario = forms.ModelChoiceField(
        queryset=CadastroUsuario.objects.all(), to_field_name="id"
    )
    data_transacao = forms.DateTimeField(widget=forms.DateInput(attrs={"type": "date"}))

    class Meta:
        model = Transacao
        fields = ["data_transacao", "status_transacao", "usuario"]


class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = [
            "numero_projeto",
            "numero_sei",
            "numero_parcela",
            "valor_solicitado",
            "titulo_projeto",
            "status_transacao",
            "transacao",
        ]


class ProcessoForm(forms.ModelForm):

    data_transacao = forms.DateTimeField(widget=forms.DateInput(attrs={"type": "date"}))
    data_solicitacao = forms.DateTimeField(
        widget=forms.DateInput(attrs={"type": "date"})
    )
    data_conferencia_documentos = forms.DateTimeField(
        widget=forms.DateInput(attrs={"type": "date"})
    )
    data_autorizacao_empenho = forms.DateTimeField(
        widget=forms.DateInput(attrs={"type": "date"})
    )
    data_confeccao_empenho = forms.DateTimeField(
        widget=forms.DateInput(attrs={"type": "date"})
    )
    data_confeccao_termo = forms.DateTimeField(
        widget=forms.DateInput(attrs={"type": "date"})
    )
    data_envio_termo = forms.DateTimeField(
        widget=forms.DateInput(attrs={"type": "date"})
    )
    data_visto_termo = forms.DateTimeField(
        widget=forms.DateInput(attrs={"type": "date"})
    )
    data_envio_term_proponente = forms.DateTimeField(
        widget=forms.DateInput(attrs={"type": "date"})
    )
    data_assinatura_termo = forms.DateTimeField(
        widget=forms.DateInput(attrs={"type": "date"})
    )
    data_envio_pagamento = forms.DateTimeField(
        widget=forms.DateInput(attrs={"type": "date"})
    )
    data_ordem_bancaria = forms.DateTimeField(
        widget=forms.DateInput(attrs={"type": "date"})
    )

    class Meta:
        model = Processo
        fields = [
            "data_solicitacao",
            "data_conferencia_documentos",
            "data_autorizacao_empenho",
            "data_confeccao_empenho",
            "numero_empenho",
            "data_confeccao_termo",
            "data_envio_termo",
            "numero_termo",
            "responsavel_confeccao",
            "data_visto_termo",
            "data_envio_term_proponente",
            "data_assinatura_termo",
            "data_envio_pagamento",
            "data_ordem_bancaria",
            "status_transacao",
            "projeto",
        ]
