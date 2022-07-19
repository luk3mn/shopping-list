from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth

from usuario.utils import validar_senha

# Cadastro de usuários
def cadastro_usuario(request):
    if request.method == "GET": # se o método de requisição for "GET"
        if request.user.is_authenticated: # se estiver logado
            return redirect('/') # redireciona para o index
        return render(request, 'usuario/cadastro-usuario.html') # renderiza o HTML de cadastro
    elif request.method == "POST":
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirme-senha')

        # valida se os campos senha são iguais
        if not validar_senha(request, senha, confirmar_senha):
            return redirect('/usuarios/cadastro')
        
        try:
            user = User.objects.create_user(username=usuario, password=senha) # inseri 'usuario' e 'senha' no banco de dados
            user.save() # salva as inserções
            return redirect('/usuarios/login') # redireciona para login se não der nenhum erro
        except:
            return HttpResponse('ERRO INTERNO!!!')

# login de usuários
def login_usuario(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'usuario/autenticacao-usuario.html')
    elif request.method == "POST":
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')

        # chama o método para autenticar o usuario
        usuario_logado = auth.authenticate(username=usuario, password=senha)

        if not usuario_logado:
            return HttpResponse("Usuario não existe")
        else:
            auth.login(request, usuario_logado) # faz o login do usuario
            return redirect('/itens')

    return HttpResponse('Login do usuario')

# para sair da conta
def sair(request):
    auth.logout(request)
    return redirect('/usuarios/login')