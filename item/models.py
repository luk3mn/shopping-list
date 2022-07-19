from django.db import models
from django.contrib.auth.models import User

# criação dos modelos de item
class Item(models.Model):
    nome_item = models.CharField(max_length=50) # guarda o nome do item
    data_adicao = models.DateTimeField(auto_now=True) # guarda a data atual
    checado = models.BooleanField(default=False) # define que o item não começa checado
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True) # chave-estrangeira para associar uma os usuarios aos itens da lista

    # define o que será exibido
    def __str__(self) -> str:
        return self.nome_item