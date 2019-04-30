"""
Crie um módulo chamado moeda.py que tenha as funções incorporadas:
aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções.

Ex.:
    >>> moeda.metade(500)
    '250.00'
    >>> moeda.dobro(500)
    '1000.00'
    >>> moeda.aumentar(500, 10)
    '550.00'
    >>> moeda.diminuir(500, 13)
    '435.00'
"""
from Desafio107 import moeda


preco = float(input('Digite o preço: R$'))
print(f'A metade de {preco} é {moeda.metade(preco)}')
print(f'O dobro  de {preco} é {moeda.dobro(preco)}')
print(f'Aumentando 10%, temos {moeda.aumentar(preco, 10)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(preco, 13)}')
