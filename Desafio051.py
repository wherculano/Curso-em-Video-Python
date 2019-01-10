'''
Desafio051: leia o primeiro termo e a
razao de uma Progressão Aritmetica.
No final mostre os 10 primeiros termos
dessa progressão
'''

num = int(input('Primeiro termo: '))
raz = int(input('Razão: '))

dec = num + (10-1) * raz #pega o decimo termo (n-esino termo da razao)
for i in range(num, dec+raz, raz):
    print('{} '.format(i), end='-> ')
    
print('FIM')
    

