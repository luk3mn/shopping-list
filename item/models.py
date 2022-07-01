from django.db import models

# criação dos modelos de item
class Item(models.Model):
    nome_item = models.CharField(max_length=50) # guarda o nome do item
    data_adicao = models.DateTimeField(auto_now=True) # guarda a data atual
    checado = models.BooleanField(default=False) # define que o item não começa checado