def metade(valor=0, format=False):
    resp = float(valor / 2)
    if format:
        return moeda(resp)
    else:
        return resp


def dobro(valor=0, format=False):
    resp = float(valor * 2)
    if format == True:
        return moeda(resp)
    else:
        return resp


def aumentar(valor, taxa=0, format=False):
    resp = float(valor + (taxa / 100 * valor))
    if format == True:
        return moeda(resp)
    else:
        return resp


def diminuir(valor, taxa=0, format=False):
    resp = float(valor - (taxa / 100 * valor))
    if format:
        return moeda(resp)
    else:
        return resp


def moeda(valor=0, cifrao='R$'):
    return f"{cifrao}{valor:.2f}".replace('.', ',')
