"""
Modifique as funções criadas no Desafio107 para que eles aceitem um parametro a mais,
informando se o valor retornado por eles vai ser ou não formatado pela função moeda(),
desenvolvida no Desafio108

Ex:
    >>> moeda.metade(500, True)
    250,00
    >>> moeda.metade(500, False)
    250.0
    >>> moeda.dobro(500)
    1000,00
    >>> moeda.aumentar(500, 10)
    550,00
    >>> moeda.diminuir(500, 13)
    435,00
"""
from Desafio107 import moeda


preco = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco, True)}')
print(f'O dobro  de {moeda.moeda(preco)} é {moeda.dobro(preco, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(preco, 10, True)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(preco, 13, True)}')

