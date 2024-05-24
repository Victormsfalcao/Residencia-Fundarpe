from django.shortcuts import render, redirect, get_object_or_404
from .forms import CadastroUsuarioForm, TransacaoForm, ProcessoForm, ProjetoForm
from .models import Projeto, Processo, CadastroUsuario, Transacao


def home(request):
    return render(request, 'home.html')

def usuarios_html(request):
    usuarios = CadastroUsuario.objects.all()
    return render(request, "usuarios.html", {"usuarios": usuarios})


def transacao_html(request):
    transacoes = Transacao.objects.all()  # Renomeando para transacoes
    return render(request, "transacao.html", {"transacoes": transacoes})  # Passando transacoes para o contexto


def projeto_html(request):
    projetos = Projeto.objects.all()
    return render(request, "projeto.html", {"projetos": projetos})

def processo_html(request):
    processos = Processo.objects.all()
    return render(request, "processo.html", {"processos": processos})

def form_cadastro_usuario(request):
    if request.method == "POST":
        form = CadastroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("usuarios_html")  # Ou redirecione para onde desejar após o cadastro
    else:
        form = CadastroUsuarioForm()
    return render(request, "form_cadastro_usuario.html", {"form": form})

def form_transacao(request):
    if request.method == "POST":
        form = TransacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("transacao_html")
    else:
        form = TransacaoForm()
    return render(request, "form_transacao.html", {"form": form})


def form_projeto(request):
    if request.method == "POST":
        form = ProjetoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("projeto.html")
    else:
        form = ProjetoForm()
    return render(request, "form_projeto.html", {"form": form})


def form_processo(request):
    if request.method == "POST":
        form = ProcessoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("processo.html")
    else:
        form = ProcessoForm()
    return render(request, "form_processo.html", {"form": form})


