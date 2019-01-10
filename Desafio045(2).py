#Desafio045 - Jokenpô (pedra, papel e tesoura)

from time import sleep
from random import choice, randint
import os

placar = {'Ganhou':0,'Perdeu':0}

def limpar():
    if os.name == 'nt':
        return  os.system('cls')
    else:
        return  os.system('clear')
        
limpar()

def img(jogador):
    if jogador == 'Pedra':
        imagem = chr(9994)
    elif jogador == 'Papel':
        imagem = chr(9995)
    elif jogador == 'Tesoura':
        imagem = chr(9996)
    return imagem

itens = ('Pedra','Papel','Tesoura')
computador = randint(0,2)
opcoes = {'Pedra':9994,'Papel':9995,'Tesoura':9996}

print('''-=-=-=-=JOKENPÔ-=-=-=-=
[0] PEDRA
[1] PAPEL
[2] TESOURA
''')

jogador = int(input('Qual sua jogada?\nOpcao: '))

print('\nJO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO\n')

print('-='*10)
print('Voce {} x {} Computador'.format(img(itens[jogador]),img(itens[computador])))
print('-='*10)

if computador == 0: #Pedra
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('VOCÊ GANHOU!')
        placar['Ganhou'] = placar.get('Ganhou')+1
    elif jogador == 2:
        print('VOCÊ PERDEU!')
        placar['Perdeu'] = placar.get('Perdeu')+1
    else:
        print('JOGADA INVÁLIDA!')
            
elif computador == 1: #Papel
    if jogador == 0:
        print('VOCÊ PERDEU!')
        placar['Perdeu'] = placar.get('Perdeu')+1
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('VOCÊ GANHOU!')
        placar['Ganhou'] = placar.get('Ganhou')+1
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2: #Tesoura
    if jogador == 0:
        print('VOCÊ GANHOU!')
        placar['Ganhou'] = placar.get('Ganhou')+1
    elif jogador == 1:
        print('VOCÊ PERDEU!')
        placar['Perdeu'] = placar.get('Perdeu')+1
    elif jogador == 2:
        print('EMPATE!')
else:
    print('JOGADA INVÁLIDA!')

print('\nVoce {} x {} PC'.format(placar.get('Ganhou'),placar.get('Perdeu')))  
#sleep(2)
#limpar()
