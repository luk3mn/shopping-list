
def validar_senha(request, senha, confirme_senha):
    if not senha == confirme_senha:
        return False

    return True