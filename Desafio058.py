#Desafio058
'''
Melhore o jogo Desafio028 onde o computador vai
'pensar' em um numero entre 0 e 10. So que agora o jogador
vai tentar adivinhar ate acertar, mostrando no final quantos
palpites dores necessarios para vencer.
'''
from random import randint

pc = randint(0,10)
cont = 0
acertou = False
print('''Olá, vamos jogar!?
Acabei de pensar em um número entre 0 e 10.
Será que você consegue acertar qual foi?''')


while not acertou:
    vc = int(input('\nQual o seu palpite?\nResp.: '))
    cont += 1
    if vc == pc:
        acertou = True
    elif vc > pc:
        print('Menor...Tente outra vez')   
    else:
        print('Maior...Tente outra vez')
print('Voce acertou com {} tentativas!'.format(cont))
