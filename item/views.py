from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from django.views.generic import ListView, CreateView, UpdateView, DeleteView # componente do CRUD
from .models import Item # importa o modelo criado para a tebela Item no db
from .forms import ItemForm
from django.contrib.auth.mixins import LoginRequiredMixin # para utilizar o login_required em 'Generic View'
from django.contrib.auth.models import User

# (READING)
def home(request):
    id_usuario = request.user.id # pega o id do usuário logado
    itens = Item.objects.filter(usuario=id_usuario) # consulta todos os itens associado ao id do usuario logado
    return render(request, 'home.html', {'itens':itens, 'id_usuario':id_usuario}) # retorna para a home incluindo na lista os itens e o id do usuario logado

def sobre(request):
    return render(request, 'about.html')

# (CREATE)
def adicionar_item(request):
    id_usuario = request.user.id # pega o id do usuário logado
    usuario = get_object_or_404(User, id=id_usuario)
    if request.method == "POST":
        item = request.POST.get('item')

        adicionar_item = Item(usuario=usuario, nome_item=item)
        adicionar_item.save()

        return redirect('/')
        # return redirect(reverse('item.home', args=[id_usuario]))

# (UPDATE)
def atualizar_item(request):
    return HttpResponse('ALTERAR NOME DO ITEM')

# (DELETE)
def remover_item(request):
    return HttpResponse('MARCAR ITEM COMO CONCLUÍDO')

# # (READING) Construção da classe para consultar os itens no db e listar com auxilo do 'ListView'
# class ListaItemView(ListView):
#     model = Item
#     queryset = Item.objects.all().order_by('data_adicao') # consulta todos os registro da tabela ordenado pelo 'nome_item'

#     # mecanismo de busca
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         queryset = queryset.filter(usuario=self.request.user) # busca os itens associados ao usuario logado
#         buscar_item = self.request.GET.get('pesquisar') or None # pega a requisição pela url (GET) com o name informado no formulario

#         # verifica se retorna algo pelo metodo GET (url)
#         if buscar_item:
#             # aplica o filtro passando o nome do item informado na models
#             queryset = queryset.filter(nome_item__contains=buscar_item)

#         return queryset

# # (CREATE)
# class ItemCreateView(LoginRequiredMixin, CreateView):
#     login_url = '/usuarios/login/'
#     model = Item # indica o modelo de referencia
#     form_class = ItemForm # indica a classe que manipula o formalário
#     success_url = '/itens/' # redireciona para 'itens'

#     def form_valid(self, form):
#         form.instance.usuario = self.request.user
#         return super().form_valid(form)

# # (UPDATE)
# class UpdateItemView(LoginRequiredMixin, UpdateView):
#     login_url = '/usuaios/login/' # -> Para
#     model = Item # referencia a tabela (classe da model) do db
#     form_class = ItemForm # passa os dados do formulario para para 'form_class'
#     success_url = '/itens/' # caso obtenho sucesso, faz o redirecionamento

# # (DELETE)
# class DeleteItemView(LoginRequiredMixin, DeleteView):
#     login_url = '/usuarios/login/'
#     model = Item # referencia a model
#     success_url = '/itens/' # faz o redirecionamento em caso de sucesso