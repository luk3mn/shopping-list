from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.messages import constants

from usuario.utils import validar_campos, validar_senha

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
        
        # valida se os campos estão em branco
        if not validar_campos(request=request, usuario=usuario, senha=senha, confirme_senha=confirmar_senha):
            return redirect('/usuarios/cadastro')

        # valida se usuario já existe no banco de dados
        if User.objects.filter(username=usuario):
            messages.add_message(request, constants.ERROR, 'Sorry! but the user already exists, better luck next time!!')
            return redirect('/usuarios/cadastro')

        try:
            user = User.objects.create_user(username=usuario, password=senha) # inseri 'usuario' e 'senha' no banco de dados
            user.save() # salva as inserções
            messages.add_message(request, constants.SUCCESS, 'Awesome! The user has been created successful')
            return redirect('/usuarios/login') # redireciona para login se não der nenhum erro
        except:
            messages.add_message(request, constants.ERROR, 'Something went wrong')
            return redirect('/usuarios/login/')

# login de usuários
def login_usuario(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'usuario/autenticacao-usuario.html')
    elif request.method == "POST":
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')

        # valida se os campos estão em branco
        if not validar_campos(request=request, usuario=usuario, senha=senha):
            return redirect('/usuarios/login')

        # chama o método para autenticar o usuario
        usuario_logado = auth.authenticate(username=usuario, password=senha)

        if not usuario_logado:
            messages.add_message(request, constants.ERROR, "Sorry, we couldn't find an account with that username or password!")
            return redirect('/usuarios/login/')
        else:
            auth.login(request, usuario_logado) # faz o login do usuario
            return redirect('/')

    # return HttpResponse('Login do usuario')

# para sair da conta
def sair(request):
    auth.logout(request)
    return redirect('/usuarios/login')