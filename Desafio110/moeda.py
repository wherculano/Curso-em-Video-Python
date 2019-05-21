def metade(valor=0, formato=False):
    resp = float(valor / 2)
    if formato:
        return moeda(resp)
    else:
        return resp


def dobro(valor=0, formato=False):
    resp = float(valor * 2)
    if formato:
        return moeda(resp)
    else:
        return resp


def aumentar(valor, taxa=0, formato=False):
    resp = float(valor + (taxa / 100 * valor))
    if format:
        return moeda(resp)
    else:
        return resp


def diminuir(valor, taxa=0, formato=False):
    resp = float(valor - (taxa / 100 * valor))
    if formato:
        return moeda(resp)
    else:
        return resp


def moeda(valor=0, cifrao='R$'):
    return f"{cifrao}{valor:.2f}".replace('.', ',')


def resumo(valor, aum=10, dim=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(valor)}')
    print(f'Dobro do preço: \t{dobro(valor, True)}')
    print(f'Metade do preço: \t{metade(valor, True)}')
    print(f'{aum}% de aumento: \t{aumentar(valor, aum, True)}')
    print(f'{dim}% de redução: \t{diminuir(valor, dim, True)}')
    print('-'*30)
