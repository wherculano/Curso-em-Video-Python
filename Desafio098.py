#Desafio098
from time import sleep

def contador(inic, fim, passo):
#	if inic > fim and passo < 0:
	#	passo *= -1
	if inic > fim and passo > 0:
		passo *= -1
	elif inic < fim and passo < 0:
		passo *= -1

	print(f'Contagem de {inic} a {fim} pulando de {passo} em {passo}.')
	for i in range(inic, fim+passo,passo):
		print(i, end=' ', flush=True)#flush evita a "bufferizacao" e mostra 1 por 1
		sleep(0.5)
	print('Fim\n')
	
	
contador(1,10,1)
contador(10,0,2)

print('Agora é sua vez!')
com = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(com,fim,passo)
