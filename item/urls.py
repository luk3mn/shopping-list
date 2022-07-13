from django.urls import path
from .views import ItemCreateView, ListaItemView, UpdateItemView, DeleteItemView # importa a classes do CRUD da views do app 'item' para realizar as tarefas no DB

urlpatterns = [
    path('', ListaItemView.as_view(), name='item.index'), # rota de leitura dos dados (listagem)
    path('novo/', ItemCreateView.as_view(), name='item.novo'), # rota de criação
    path('editar/<int:pk>', UpdateItemView.as_view(), name='item.editar'), # rota de edição
    path('remover/<int:pk>', DeleteItemView.as_view(), name='item.remover')
]