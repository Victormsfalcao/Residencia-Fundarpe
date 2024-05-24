from django.shortcuts import render, redirect, get_object_or_404
from .forms import CadastroUsuarioForm, TransacaoForm, ProcessoForm, ProjetoForm
from .models import Projeto, Processo, CadastroUsuario, Transacao


def home(request):
    return render(request, 'home.html')

def usuarios_html(request):
    usuarios = CadastroUsuario.objects.all()
    return render(request, "usuarios.html", {"usuarios": usuarios})

def transacao_html(request):
    transacao = Transacao.objects.all()
    return render(request, "transacao.html", {"transacao": transacao})

def projeto_html(request):
    projeto = Projeto.objects.all()
    return render(request, "projeto.html", {"projeto": projeto})

def processo_html(request):
    processo = Processo.objects.all()
    return render(request, "processo.html", {"processo": processo})

def form_cadastro_usuario(request):
    if request.method == "POST":
        form = CadastroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")  # Ou redirecione para onde desejar após o cadastro
    else:
        form = CadastroUsuarioForm()
    return render(request, "form_cadastro_usuario.html", {"form": form})

def form_transacao(request):
    if request.method == "POST":
        form = TransacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = TransacaoForm()
    return render(request, "transacao.html", {"form": form})


def form_projeto(request):
    if request.method == "POST":
        form = ProjetoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = ProjetoForm()
    return render(request, "projeto.html", {"form": form})


def form_processo(request):
    if request.method == "POST":
        form = ProcessoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = ProcessoForm()
    return render(request, "processo.html", {"form": form})


