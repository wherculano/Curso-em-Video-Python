#Desafio28
import random
from time import sleep

n = random.randint(0,5)
op = int(input('\nDigite um numero entre 0 e 5: '))
print('\nLoading...')
sleep(3) #espera 3 segundos para mostrar a linha abaixo
print('\nPC = {}     Você = {}'.format(n, op))

if n == op:
    print('\nParabens! Você acertou o número')
else:
    print('\nQue pena, você errou!')
    
