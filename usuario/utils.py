from django.contrib import messages
from django.contrib.messages import constants

def validar_senha(request, senha, confirme_senha):
    if not senha == confirme_senha:
        messages.add_message(request, constants.ERROR, "Ops! It seems you are trying to put passwords that don't match, let's go again!!")
        return False
    
    return True

def validar_campos(request, usuario, senha, confirme_senha=None):
    if usuario == "" or senha == "":
        messages.add_message(request, constants.ERROR, "Hey, have you not forgotten something? If I were in your shoes I would fill up all the fields")
        return False
    
    return True