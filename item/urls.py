from django.urls import path
from .views import ItemCreateView, ListaItemView, UpdateItemView, DeleteItemView # importa a classes do CRUD da views do app 'item' para realizar as tarefas no DB
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(ListaItemView.as_view()), name='item.index'), # rota de leitura dos dados (listagem)
    path('novo/', login_required(ItemCreateView.as_view()), name='item.novo'), # rota de criação
    path('editar/<int:pk>', login_required(UpdateItemView.as_view()), name='item.editar'), # rota de edição
    path('remover/<int:pk>', login_required(DeleteItemView.as_view()), name='item.remover')
]