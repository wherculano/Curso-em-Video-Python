#Desafio100

from random import randint
from time import sleep


def sorteia(lista):
	print('-='*21)
	print('Sorteando os numeros ...')
	for i in range(5):
		rand = randint(0,10)
		print(rand, end=' ',flush=True)
		sleep(0.5)
		lista.append(rand)
	print(f'\nOs numeros sorteados foram {lista}')


def somaPar(lista):
	soma = 0
	print('-='*21)
	print('Os numeros pares sao: ',end='')
	for i in lista:
		if i % 2 == 0:
			print(i, end=' ', flush=True)
			soma += i
	print(f'\nE a soma entre eles é {soma}')


numeros = []

sorteia(numeros)

somaPar(numeros)
		