"""
Modifique as funções criadas no Desafio107 para que eles aceitem um parametro a mais,
informando se o valor retornado por eles vai ser ou não formatado pela função moeda(),
desenvolvida no Desafio108

Ex:
    >>> moeda.metade(500, True)
    'R$250,00'
    >>> moeda.metade(500, False)
    250.0
    >>> moeda.dobro(500, True)
    'R$1000,00'
    >>> moeda.dobro(500)
    1000.0
    >>> moeda.aumentar(500, 10, True)
    'R$550,00'
    >>> moeda.aumentar(500, 10)
    550.0
    >>> moeda.diminuir(500, 13, True)
    'R$435,00'
    >>> moeda.diminuir(500, 13)
    435.0
"""
from Desafio109 import moeda


preco = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco, True)}')
print(f'O dobro  de {moeda.moeda(preco)} é {moeda.dobro(preco, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(preco, 10, True)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(preco, 13, True)}')

