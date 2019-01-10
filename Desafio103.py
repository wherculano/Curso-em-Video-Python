#Desafio103.py
'''
Faça um programa que tenha uma função chamada ficha(), que receba dois parametros
opcionais: o nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado
não tenha sido informado corretamente.

Nome do Jogador: Romario
Numero de Gols: 33
O jogador ROmario fez 33 gol(s) no campeonato

Nome do Jogador: 
Numero de Gols: 10
O jogador <desconhecido> fez 10 gol(s) no campeonato

Nome do Jogador: 
Numero de Gols: 
O jogador <desconhecido> fez 0 gol(s) no campeonato
'''

def ficha(nome=None, gols = None):
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    if nome.strip() == '':
        nome = '<desconhecido>'
    return f'O jogador {nome} marcou {gols} gols.'



n = input('Nome do jogador: ')
g = input('Gols marcados: ')

print(ficha(n, g))
