#Desafio099
from time import sleep

def maior(*num):
	cont = maior = 0
	print('-='*20)
	print('Analisando os numeros ...')
	for n in num:
		print(n,end=' ',flush=True)
		sleep(0.5)
		if cont == 0:
			maior = n
		else:
			if n > maior:
				maior = n
		cont += 1			
	print(f'\nForam passados {cont} numeros e o maior foi o {maior}')
	#print()
	#print('-='*20)


maior(1,3,5,8)
maior(7,0,1,5,9,3,2,6)
maior()
maior(9)
		