from django.shortcuts import render

from django.views.generic import ListView # componente para listagem
from .models import Item # importa o modelo criado para a tebela Item no db

# Construção da classe para consultar os itens no db e listar com auxilo do 'ListView'
class ListaItemView(ListView):
    model = Item
    queryset = Item.objects.all().order_by('nome_item') # consulta todos os registro da tabela ordenado pelo 'nome_item'