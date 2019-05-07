"""
Adicione uao módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas
ingormações geradas pelas funções que já temos no módulo criado até aqui.

Ex:
    >>> moeda.resumo(500, 80, 35)
    ----------------------------------
             RESUMO DO VALOR
    ----------------------------------
    Preço analisado:        R$500,00
    Dobro do preço:         R$1000,00
    Metade do preço:        R$250,00
    80% de aumento:         R$900,00
    35% de redução:         R$325,00
    ----------------------------------
"""
from Desafio110 import moeda


preco = float(input('Digite o preço: R$'))
moeda.resumo(preco, 80, 35)
