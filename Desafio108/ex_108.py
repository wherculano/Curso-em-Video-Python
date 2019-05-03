"""
Adapte o código do Desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os
valores como um valor monetário formatado.

Ex:
    >>> moeda.moeda(moeda.metade(500))
    'R$250,00'
    >>> moeda.moeda(moeda.dobro(500))
    'R$1000,00'
    >>> moeda.moeda(moeda.aumentar(500, 10))
    'R$550,00'
    >>> moeda.moeda(moeda.diminuir(500, 13))
    'R$435,00'
"""
from Desafio108 import moeda


preco = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}')
print(f'O dobro  de {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(preco, 10))}')
print(f'Reduzindo 13%, temos {moeda.moeda(moeda.diminuir(preco, 13))}')
