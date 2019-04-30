def metade(valor):
    resp = valor / 2
    return f'{resp:.2f}'


def dobro(valor):
    resp = valor * 2
    return f'{resp:.2f}'


def aumentar(valor, taxa=0):
    resp = valor + (taxa / 100 * valor)
    return f'{resp:.2f}'


def diminuir(valor, taxa=0):
    resp = valor - (taxa / 100 * valor)
    return f'{resp:.2f}'


def moeda(valor):
    return f"R${str(valor).replace('.', ',')}"
