#Desafio045 - Jokenpô (pedra, papel e tesoura)
import time
placar = {'Ganhou':0,'Perdeu':0}

from random import choice, randint
import os

def limpar():
    if os.name == 'nt':
        return  os.system('cls')
    else:
        return  os.system('clear')
        
limpar()

lista = ['Pedra','Papel','Tesoura']
opcoes = {'Pedra':9994,'Papel':9995,'Tesoura':9996}
escolha = 0

while escolha != 4:
    print('\n\033[7;35;47m','-'*10,'JOKENPÔ','-'*10,'\033[m\n',end='')
    
    print('\nVoce \033[1;33m{} x {}\033[m PC'.format(placar.get('Ganhou'),placar.get('Perdeu')))
    
    print('\n1- {}Pedra\n2- {}Papel\n3- {}Tesoura\n4- SAIR'.format(chr(9994),chr(9995),chr(9996)))
    
    try:
        escolha=int(input('Opcao: '))
    except:
        print('\nOpcao inválida!\nUma opcao aleatoria\nserá escolhida para você ')
        escolha = randint(1,3)
        
    pc = opcoes.get(choice(lista))
    jogador = None

    if escolha == 1:
        jogador = 9994
    elif escolha == 2:
        jogador = 9995
    elif escolha == 3:
        jogador = 9996
    elif escolha == 4:
        print('Saindo....')
        break
    else:
        print('\nOpção inválida!\nUma opcao aleatoria será\nescolhida para você')
        jogador = randint(9994,9996)
    print()

    if jogador == pc:
        print(chr(jogador),'x',chr(pc))
        print('Empate\n')
        #placar['Perdeu'] = placar.get('Perdeu')+1
        #placar['Ganhou'] = placar.get('Ganhou')+1
    elif (jogador == 9994 and pc == 9996) or (jogador == 9995 and pc == 9994) or (jogador == 9996 and pc == 9995):
        print(chr(jogador),'x',chr(pc))
        print('Voce ganhou\n')
        placar['Ganhou'] = placar.get('Ganhou')+1
    else:
        print(chr(jogador),'x',chr(pc))
        print('Voce perdeu\n')
        placar['Perdeu'] = placar.get('Perdeu')+1
    
    time.sleep(2)
    limpar()

