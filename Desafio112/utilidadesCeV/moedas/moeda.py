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


def resumo(valor, aum, dim):
    msg = '         RESUMO DO VALOR'
    print('-'*(len(msg)+10))
    print(msg)
    print('-'*(len(msg)+10))
    print(f'Preço analisado:\t\t{moeda(valor)}')
    print(f'Dobro do preço:\t\t\t{moeda(dobro(valor))}')
    print(f'Metade do preço:\t\t{moeda(metade(valor))}')
    print(f'{aum}% de aumento:\t\t\t{moeda(aumentar(valor, aum))}')
    print(f'{dim}% de redução:\t\t\t{moeda(diminuir(valor, dim))}')
    print('-'*(len(msg)+10))
