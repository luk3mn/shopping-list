from django.urls import path
from .views import HomeView # importa a classe 'HomeView' da views do app 'main' para renderizar a página principal (index) do site

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]