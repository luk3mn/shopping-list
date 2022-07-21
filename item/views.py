from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from django.views.generic import ListView, CreateView, UpdateView, DeleteView # componente do CRUD
from .models import Item # importa o modelo criado para a tebela Item no db
from .forms import ItemForm
from django.contrib.auth.mixins import LoginRequiredMixin # para utilizar o login_required em 'Generic View'
from django.contrib.auth.models import User

# (READING) Construção da classe para consultar os itens no db e listar com auxilo do 'ListView'
class ListaItemView(ListView):
    model = Item
    queryset = Item.objects.all().order_by('nome_item') # consulta todos os registro da tabela ordenado pelo 'nome_item'

    # mecanismo de busca
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(usuario=self.request.user) # busca os itens associados ao usuario logado
        buscar_item = self.request.GET.get('pesquisar') or None # pega a requisição pela url (GET) com o name informado no formulario

        # verifica se retorna algo pelo metodo GET (url)
        if buscar_item:
            # aplica o filtro passando o nome do item informado na models
            queryset = queryset.filter(nome_item__contains=buscar_item)

        return queryset

# (CREATE)
class ItemCreateView(LoginRequiredMixin, CreateView):
    login_url = '/usuarios/login/'
    model = Item # indica o modelo de referencia
    form_class = ItemForm # indica a classe que manipula o formalário
    success_url = '/itens/' # redireciona para 'itens'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

# def itens(request, pk_item):
#     itens = Item.objects.filter(usuario=pk_item)
#     return render(request, 'item/item_list.html', {'itens':itens, 'pk_item':pk_item})

def adicionar_item(request):
    # usuario = get_object_or_404(Item, id=id_item)
    # usuarios = Item.objects.filter(usuario=pk_item)
    id_usuario = User.objects.filter(id=7) # ===== CONTINUAR DAQUI ====
    # usuario = Item(usuario=request.user)
    if request.method == "POST":
        item = request.POST.get('item')

        adicionar_item = Item(nome_item=item)
        adicionar_item.save()

        # return redirect('/itens/')
        return HttpResponse(id_usuario)

# (UPDATE)
class UpdateItemView(LoginRequiredMixin, UpdateView):
    login_url = '/usuaios/login/' # -> Para
    model = Item # referencia a tabela (classe da model) do db
    form_class = ItemForm # passa os dados do formulario para para 'form_class'
    success_url = '/itens/' # caso obtenho sucesso, faz o redirecionamento

# (DELETE)
class DeleteItemView(LoginRequiredMixin, DeleteView):
    login_url = '/usuarios/login/'
    model = Item # referencia a model
    success_url = '/itens/' # faz o redirecionamento em caso de sucesso