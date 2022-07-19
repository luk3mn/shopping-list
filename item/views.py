from django.shortcuts import render

from django.views.generic import ListView, CreateView, UpdateView, DeleteView # componente do CRUD
from .models import Item # importa o modelo criado para a tebela Item no db
from .forms import ItemForm
from django.contrib.auth.decorators import login_required

# (READING) Construção da classe para consultar os itens no db e listar com auxilo do 'ListView'
# @login_required(login_url='/usuarios/login/')
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
class ItemCreateView(CreateView):
    model = Item # indica o modelo de referencia
    form_class = ItemForm # indica a classe que manipula o formalário
    success_url = '/itens/' # redireciona para 'itens'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

# (UPDATE)
class UpdateItemView(UpdateView):
    model = Item # referencia a tabela (classe da model) do db
    form_class = ItemForm # passa os dados do formulario para para 'form_class'
    success_url = '/itens/' # caso obtenho sucesso, faz o redirecionamento

# (DELETE)
class DeleteItemView(DeleteView):
    model = Item # referencia a model
    success_url = '/itens/' # faz o redirecionamento em caso de sucesso