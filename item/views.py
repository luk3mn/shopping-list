from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from datetime import date
from django.views.generic import ListView, CreateView, UpdateView, DeleteView # componente do CRUD
from .models import Item # importa o modelo criado para a tebela Item no db
from .forms import ItemForm
from django.contrib.auth.mixins import LoginRequiredMixin # para utilizar o login_required em 'Generic View'
from django.contrib.auth.models import User

# (READING)
def home(request):
    id_usuario = request.user.id # pega o id do usuário logado
    itens = Item.objects.filter(usuario=id_usuario) # consulta todos os itens associado ao id do usuario logado
    return render(request, 'home.html', {'data':date.today,'itens':itens, 'id_usuario':id_usuario}) # retorna para a home incluindo na lista os itens e o id do usuario logado

def sobre(request):
    return render(request, 'about.html')

# (CREATE)
def adicionar_item(request, id_usuario):
    # id_usuario = request.user.id # pode pegar o id diretamente, mas nesse caso está puxando pelo GET vindo da url
    usuario = get_object_or_404(User, id=id_usuario)
    if request.method == "POST": # verifica se o método de requisição é POST
        item = request.POST.get('item') # pega o nome do item vindo do formulário pelo POST

        # instancia a model do banco de dados passando para ela o id do usuario (FK) e o nome do item
        adicionar_item = Item(usuario=usuario, nome_item=item)
        adicionar_item.save() # salva no banco de dados

    return redirect('/')

# (UPDATE)
def atualizar_item(request):
    return HttpResponse('ALTERAR NOME DO ITEM')

# (DELETE)
def remover_item(request, id_item):
    item = get_object_or_404(Item, id=id_item)
    if id_item == item.id:
        marcar_item = Item(id=id_item) # remove o item do banco
        marcar_item.save() # salva no banco de dados
        return redirect('/')
    else:
        return HttpResponse("Não existe")

def verificar_item(request, id_item):
    # item = Item.objects.get(id=id_item) # primeira forma de acessar os valores do banco
    item = get_object_or_404(Item, id=id_item) # segunda forma de acessar os valores do banco
    item.checado = True # altera o valor do campo 'checado' para True
    item.save() # salva no banco

    return redirect('/') # redireciona para o index

# ANOTAÇÔES:
# - Verificar a opção de remover
# - Add a opção de edição
# - Fazer as validações
# - Melhorar a visualização da lista