def metade(valor=0):
    resp = float(valor / 2)
    return resp


def dobro(valor=0):
    resp = float(valor * 2)
    return resp


def aumentar(valor=0, taxa=0):
    resp = float(valor + (taxa / 100 * valor))
    return resp


def diminuir(valor=0, taxa=0):
    resp = float(valor - (taxa / 100 * valor))
    return resp


def moeda(valor=0, cifrao="R$"):
    return f"{cifrao}{valor:.2f}".replace('.', ',')

