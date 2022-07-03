from django.shortcuts import render

from django.views.generic import ListView, CreateView # componente para listagem
from .models import Item # importa o modelo criado para a tebela Item no db
from .forms import ItemForm

# Construção da classe para consultar os itens no db e listar com auxilo do 'ListView'
class ListaItemView(ListView):
    model = Item
    queryset = Item.objects.all().order_by('nome_item') # consulta todos os registro da tabela ordenado pelo 'nome_item'

class ItemCreateView(CreateView):
    model = Item # indica o modelo de referencia
    form_class = ItemForm # indica a classe que manipula o formalário
    success_url = '/itens/' # redireciona para 'itens'