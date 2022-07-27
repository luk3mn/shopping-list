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

        usuario_cad = User.objects.filter(username=usuario)
        print(type(usuario_cad), type(usuario))
        return HttpResponse(usuario_cad)
        # if usuario == usuario_cad:
            # messages.add_message(request, constants.ERROR, 'Usuário já existe!')
            # return redirect('/usuarios/cadastro')
        # for user in usuarios:

        try:
            user = User.objects.create_user(username=usuario, password=senha) # inseri 'usuario' e 'senha' no banco de dados
            user.save() # salva as inserções
            messages.add_message(request, constants.SUCCESS, 'Usuário cadastrado com sucesso')
            return redirect('/usuarios/login') # redireciona para login se não der nenhum erro
        except:
            messages.add_message(request, constants.ERROR, 'Erro Interno do Sistema')
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
            messages.add_message(request, constants.ERROR, 'Usuário e/ou Senha incorretos')
            return redirect('/usuarios/login/')
        else:
            auth.login(request, usuario_logado) # faz o login do usuario
            return redirect('/')

    # return HttpResponse('Login do usuario')

# para sair da conta
def sair(request):
    auth.logout(request)
    return redirect('/usuarios/login')