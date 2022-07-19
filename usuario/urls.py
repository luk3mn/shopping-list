from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro_usuario, name='usuario.cadastro'),
    path('login/', views.login_usuario, name='usuario.login'),
    path('sair/', views.sair, name='usuario.sair'),
]