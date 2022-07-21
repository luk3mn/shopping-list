from django.urls import path
from .views import ItemCreateView, ListaItemView, UpdateItemView, DeleteItemView # importa a classes do CRUD da views do app 'item' para realizar as tarefas no DB
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # na url de itens é utilizado o login required passando o segundo parâmetro indicando o caminho
    path('', login_required(ListaItemView.as_view(), login_url='/usuarios/login/'), name='item.index'), # rota de leitura dos dados (listagem)
    # em 'novo', 'editar' e 'remover' foi utilizado o 'LoginRequiredMixin' que faz o mesmo que o 'login_required', porem em Generic Views
    path('novo/', ItemCreateView.as_view(), name='item.novo'), # rota de criação
    path('adicionar/', views.adicionar_item, name="item.adicionar"),
    path('editar/<int:pk>', UpdateItemView.as_view(), name='item.editar'), # rota de edição
    path('remover/<int:pk>', DeleteItemView.as_view(), name='item.remover')
]