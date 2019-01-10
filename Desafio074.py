#--MUNDO 3--
#Desafio 74
'''
Crie um programa que vai gerar 5 numeros aleatórios e colocar em uma Tupla.
Depois disso, mostre a listagem de numeros gerados e também indique o menor e o maior valor que estão na tupla.
'''
from random import randint

num = tuple(randint(1,10) for i in range(5))
print('Os numeros aleatórios são: {}'.format(num))
print('O maior valor sorteado foi: {}'.format(max(num)))
print('O menor valor sorteado foi: {}'.format(min(num)))


