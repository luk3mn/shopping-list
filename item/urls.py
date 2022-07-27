from django.urls import path
# from .views import ItemCreateView, ListaItemView, UpdateItemView, DeleteItemView # importa a classes do CRUD da views do app 'item' para realizar as tarefas no DB
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.home, name="item.home"),
    path('sobre/', views.sobre, name="item.about"),
    path('adicionar/<int:id_usuario>/', views.adicionar_item, name="item.adicionar"),
    # path('atualizar/', views.atualizar_item, name="item.atualizar"),
    path('remover/<int:id_item>/', views.remover_item, name="item.remover"),
    path('marcar/<int:id_item>/', views.verificar_item, name="item.verificar"),
]