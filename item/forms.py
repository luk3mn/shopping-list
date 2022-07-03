from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item # referencia a model em questão
        fields = ['nome_item','checado'] # o campo 'data_adicao' está pegando a data autal, então não precisa adicionar
        