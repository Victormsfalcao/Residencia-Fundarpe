from django.db import models


class CadastroUsuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    senha = models.CharField(max_length=10)
    setor = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Transacao(models.Model):
    data_transacao = models.DateTimeField()
    status_transacao = models.CharField(max_length=100)
    usuario = models.ForeignKey(CadastroUsuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.status_transacao} em {self.data_transacao}"


class Projeto(models.Model):
    numero_projeto = models.CharField(max_length=30)
    numero_sei = models.CharField(max_length=21)
    numero_parcela = models.CharField(max_length=20)
    valor_solicitado = models.FloatField()
    titulo_projeto = models.CharField(max_length=100)
    status_transacao = models.CharField(max_length=100)
    transacao = models.ForeignKey(Transacao, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo_projeto


class Processo(models.Model):
    data_solicitacao = models.DateTimeField()
    data_conferencia_documentos = models.DateTimeField()
    data_autorizacao_empenho = models.DateTimeField()
    data_confeccao_empenho = models.DateTimeField()
    numero_empenho = models.CharField(max_length=30)
    data_confeccao_termo = models.DateTimeField()
    data_envio_termo = models.DateTimeField()
    numero_termo = models.CharField(max_length=30)
    responsavel_confeccao = models.CharField(max_length=100)
    data_visto_termo = models.DateTimeField()
    data_envio_term_proponente = models.DateTimeField()
    data_assinatura_termo = models.DateTimeField()
    data_envio_pagamento = models.DateTimeField()
    data_ordem_bancaria = models.DateTimeField()
    status_transacao = models.CharField(max_length=100)
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)

    def __str__(self):
        return f"Processo {self.numero_empenho}"
