#Desafio091
"""
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatorios. Guarde esses resultados em um dicionario. No final coloque esse dicionario em ordem, sabendo que o vencedor tirou o maior numero no dado.

>>> Valores Sorteados
>>> O jogador1 tirou ...
>>> ...
>>> Ranking dos Jogadores
>>> 1o Lugar:  Jogador1 com ...
>>> ...
"""
from time import sleep
from random import randint
from operator import itemgetter

jogadas= {}
for i in range(1,5):
	jogadas["Jogador"+str(i)] = randint(1,6)

print('VALORES SORTEADOS'.center(30,'='))
for k, v in jogadas.items():
	print(f"   {k} tirou {v}")
	sleep(1)
	
print('RANKING DOS JOGADORES'.center(30,'='))

#sorted(quemVouOrdernar, ordernarPorValor(0paraChave1paraValor), ordemDecrescente)
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)

for k, v in enumerate(ranking):
	print(f'   {k+1}o Lugar: {v[0]} com {v[1]} pontos')
	sleep(1)

