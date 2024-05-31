from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CadastroUsuarioForm, LoginForm, TransacaoForm, ProcessoForm, ProjetoForm
from .models import Projeto, Processo, CadastroUsuario, Transacao
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.models import User

@login_required
def home(request):
    user = request.user
    return render(request, 'home.html', {'user': user})

@login_required
def usuarios_html(request):
    usuarios_list = CadastroUsuario.objects.all()
    paginator = Paginator(usuarios_list, 5)

    page = request.GET.get('page')
    try:
        usuarios = paginator.page(page)
    except PageNotAnInteger:

        usuarios = paginator.page(1)
    except EmptyPage:

        usuarios = paginator.page(paginator.num_pages)

    return render(request, "usuarios.html", {"usuarios": usuarios})


@login_required
def transacao_html(request):
    transacoes_list = Transacao.objects.all()
    paginator = Paginator(transacoes_list, 5)

    page = request.GET.get('page')
    try:
        transacoes = paginator.page(page)
    except PageNotAnInteger:

        transacoes = paginator.page(1)
    except EmptyPage:

        transacoes = paginator.page(paginator.num_pages)

    return render(request, "transacao.html", {"transacoes": transacoes})

@login_required
def projeto_html(request):
    projetos_list = Projeto.objects.all()
    paginator = Paginator(projetos_list, 5)

    page = request.GET.get('page')
    try:
        projetos = paginator.page(page)
    except PageNotAnInteger:
        projetos = paginator.page(1)
    except EmptyPage:
        projetos = paginator.page(paginator.num_pages)

    return render(request, "projeto.html", {"projetos": projetos})

@login_required
def processo_html(request):
    processos_list = Processo.objects.all()
    paginator = Paginator(processos_list, 5)

    page = request.GET.get('page')
    try:
        processos = paginator.page(page)
    except PageNotAnInteger:
        processos = paginator.page(1)
    except EmptyPage:
        processos = paginator.page(paginator.num_pages)

    return render(request, "processo.html", {"processos": processos})

@login_required
def escolhas_UAFF(request):
    if request.method == "POST":
        form = ProcessoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("processo_html")
    else:
        form = ProcessoForm()
    return render(request, 'escolhas_UAFF.html', {'form': form})

@login_required
def confeccaoTermo(request):
    if request.method == "POST":
        form = ProcessoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("processo_html")
    else:
        form = ProcessoForm()
    return render(request, 'confeccaoTermo.html', {'form': form})

@login_required
def envioTermo(request):
    if request.method == "POST":
        form = ProcessoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("processo_html")
    else:
        form = ProcessoForm()
    return render(request, 'envioTermo.html', {'form': form})

@login_required
def recebimentoDoc(request):
    if request.method == "POST":
        form = ProcessoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("processo_html")
    else:
        form = ProcessoForm()
    return render(request, 'recebimentoDoc.html', {'form': form})


def form_cadastro_usuario(request):
    if request.method == "POST":
        form = CadastroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = CadastroUsuarioForm()
    return render(request, "form_cadastro_usuario.html", {"form": form})

def form_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            senha = form.cleaned_data.get("senha")
            try:
                usuario = CadastroUsuario.objects.get(email=email)
                if usuario.senha == senha:
                    user, created = User.objects.get_or_create(username=email)
                    if created:
                        user.set_password(senha)
                        user.save()
                    login(request, user)
                    request.session["setor"] = usuario.setor
                    return redirect("home")
                else:
                    messages.error(request, "Senha incorreta")
            except CadastroUsuario.DoesNotExist:
                messages.error(request, "Usuário não encontrado")
        else:
            messages.error(request, "Dados inválidos. Por favor, verifique novamente.")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})

def form_logout(request):
    logout(request)
    response = redirect('login')
    response.delete_cookie('sessionid')
    return response

@login_required
def form_transacao(request):
    if request.method == "POST":
        form = TransacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("transacao_html")
    else:
        form = TransacaoForm()
    return render(request, "form_transacao.html", {"form": form})


@login_required
def form_projeto(request):
    if request.method == "POST":
        form = ProjetoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("projeto_html")
    else:
        form = ProjetoForm()
    return render(request, "form_projeto.html", {"form": form})


@login_required
def form_processo(request):
    if request.method == "POST":
        form = ProcessoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("processo_html")
    else:
        form = ProcessoForm()
    return render(request, "form_processo.html", {"form": form})

@login_required
def edit_usuario(request, usuario_id):
    usuario = get_object_or_404(CadastroUsuario, pk=usuario_id)
    if request.method == 'POST':
        form = CadastroUsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('usuarios_html')  #
    else:
        form = CadastroUsuarioForm(instance=usuario)
    return render(request, 'edit_usuario.html', {'form': form})

@login_required
def edit_projeto(request, projeto_id):
    projeto = get_object_or_404(Projeto, pk=projeto_id)
    if request.method == 'POST':
        form = ProjetoForm(request.POST, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('projeto_html')
    else:
        form = ProjetoForm(instance=projeto)
    return render(request, 'edit_projeto.html', {'form': form})

@login_required
def edit_processo(request, processo_id):
    processo = get_object_or_404(Processo, pk=processo_id)
    if request.method == 'POST':
        form = ProcessoForm(request.POST, instance=processo)
        if form.is_valid():
            form.save()
            return redirect('processo_html')
    else:
        form = ProcessoForm(instance=processo)
    return render(request, 'edit_processo.html', {'form': form})

@login_required
def view_usuario(request, usuario_id):
    usuario = get_object_or_404(CadastroUsuario, pk=usuario_id)
    return render(request, 'view_usuario.html', {'usuario': usuario})

@login_required
def view_transacao(request, transacao_id):
    transacao = get_object_or_404(Transacao, pk=transacao_id)
    return render(request, 'view_transacao.html', {'transacao': transacao})

@login_required
def view_projeto(request, projeto_id):
    projeto = get_object_or_404(Projeto, pk=projeto_id)
    return render(request, 'view_projeto.html', {'projeto': projeto})

@login_required
def view_processo(request, processo_id):
    processo = get_object_or_404(Processo, pk=processo_id)
    return render(request, 'view_processo.html', {'processo': processo})

@login_required
def delete_usuario(request, id):
    usuario = CadastroUsuario.objects.get(pk=id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('usuarios_html')
    return render(request, 'usuarios.html', {'usuario': usuario})

@login_required
def delete_transacao(request, id):
    transacao = Transacao.objects.get(pk=id)
    if request.method == 'POST':
        transacao.delete()
        return redirect('transacao_html')
    return render(request, 'transacao.html', {'transacao': transacao})

@login_required
def delete_projeto(request, id):
    projeto = Projeto.objects.get(pk=id)
    if request.method == 'POST':
        projeto.delete()
        return redirect('projeto_html')
    return render(request, 'projeto.html', {'projeto': projeto})

@login_required
def delete_processo(request, id):
    processo = Processo.objects.get(pk=id)
    if request.method == 'POST':
        processo.delete()
        return redirect('processo_html')
    return render(request, 'processo.html', {'processo': processo})