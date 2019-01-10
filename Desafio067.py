'''
Desafio67 - Faça um programa que mostre a tabuada de varios numeros,
um de cada vez, para cada valor digitado pelo usuario. O programa ser
interrompido quando o numero solicitado for negativo.
'''

print('-'*40)
n = int(input('Quer ver a tabuada de qual numero: '))
print('-'*40)
while n > -1:
    if n < 0:
        break
    for i in range(1,11):
        print(f'{n} x {i} = {n*i}')
    print('-'*40)
    n = int(input('Quer ver a tabuada de qual numero: '))
    print('-'*40)
   
