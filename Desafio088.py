"""
Desafio088 - Faça um programa que ajude um jogador da MegaSena a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 numeros
entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""

from random import randint
#poderia usar o sample no lugar do randint, ele cria uma lista de listas
# e sem a necessidade do set
print('-='*15)
print('{: ^30}'.format('JOGO DA MEGA SENA'))
print('-='*15)

vezes = int(input('Quantos jogos você quer que eu sorteie? '))
print('\n{:=^30}'.format(' SORTEANDO '+str(vezes)+' JOGOS '))

for i in range(vezes):
    jogo = set([randint(1,60) for x in range(6)])
    jogo = list(jogo)
    jogo.sort()
    print('Jogo {}: {}'.format((i+1), jogo))
    
print('\n{:-^34}'.format('< BOA SORTE !>'))
