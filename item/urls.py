from django.urls import path
from .views import ItemCreateView, ListaItemView # importa a classe 'ListaItemView' da views do app 'item' para renderizar a página de itens do site

urlpatterns = [
    path('', ListaItemView.as_view(), name='item.index'),
    path('novo/', ItemCreateView.as_view(), name='item.novo'),
]