"""
Dentro do pacote utilidadesCeV que criamos no desafio111, temos um módulo chamado dado. Crie uma função chamada
leiaDinheiro() que seja capaz de funcionar como a funçãi input(), mas com uma validação de dados para aceitar
apenas valores que sejam monetários.

Ex:
    >>> moeda.resumo(850, 35, 22)
    ----------------------------------
             RESUMO DO VALOR
    ----------------------------------
    Preço analisado:        R$850,00
    Dobro do preço:         R$1700,00
    Metade do preço:        R$425,00
    35% de aumento:         R$1147,50
    22% de redução:         R$663,00
    ----------------------------------
"""
from Desafio112.utilidadesCeV import dados, moeda


preco = dados.leiaDinheiro('Digite o preço: R$')
moeda.resumo(preco, 35, 22)
