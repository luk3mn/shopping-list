from django.contrib import messages
from django.contrib.messages import constants

def validar_senha(request, senha, confirme_senha):
    if not senha == confirme_senha:
        messages.add_message(request, constants.ERROR, 'Senhas não coincidem!')
        return False
    
    return True

def validar_campos(request, usuario, senha, confirme_senha=None):
    if usuario == "" or senha == "":
        messages.add_message(request, constants.ERROR, 'Preencha todos os campos!')
        return False
    
    return True