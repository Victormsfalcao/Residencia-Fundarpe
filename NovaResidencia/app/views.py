from django.shortcuts import render, redirect, get_object_or_404
from .forms import CadastroUsuarioForm, TransacaoForm, ProcessoForm, ProjetoForm
from .models import Projeto, Processo, CadastroUsuario, Transacao
from django.http import JsonResponse


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

def edit_usuario(request, usuario_id):
    usuario = get_object_or_404(CadastroUsuario, pk=usuario_id)
    if request.method == 'POST':
        form = CadastroUsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('usuarios_html')  # Redireciona para a página de usuários após a edição
    else:
        form = CadastroUsuarioForm(instance=usuario)
    return render(request, 'edit_usuario.html', {'form': form})

def edit_projeto(request, projeto_id):
    projeto = get_object_or_404(Projeto, pk=projeto_id)
    if request.method == 'POST':
        form = ProjetoForm(request.POST, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('projeto_html')  # Redireciona para a página de usuários após a edição
    else:
        form = ProjetoForm(instance=projeto)
    return render(request, 'edit_projeto.html', {'form': form})

def edit_processo(request, processo_id):
    processo = get_object_or_404(Processo, pk=processo_id)
    if request.method == 'POST':
        form = ProcessoForm(request.POST, instance=processo)
        if form.is_valid():
            form.save()
            return redirect('processo_html')  # Redireciona para a página de usuários após a edição
    else:
        form = ProcessoForm(instance=processo)
    return render(request, 'edit_processo.html', {'form': form})

def view_usuario(request, usuario_id):
    usuario = get_object_or_404(CadastroUsuario, pk=usuario_id)
    return render(request, 'view_usuario.html', {'usuario': usuario})

def view_transacao(request, transacao_id):
    transacao = get_object_or_404(Transacao, pk=transacao_id)
    return render(request, 'view_transacao.html', {'transacao': transacao})

def view_projeto(request, projeto_id):
    projeto = get_object_or_404(Projeto, pk=projeto_id)
    return render(request, 'view_projeto.html', {'projeto': projeto})

def view_processo(request, processo_id):
    processo = get_object_or_404(Processo, pk=processo_id)
    return render(request, 'view_processo.html', {'processo': processo})
