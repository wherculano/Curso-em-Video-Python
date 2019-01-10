"""
Desafio085 - Crie um programa onde o usuário possa digitar 7 valores numericos
e cadastre-os em uma lista única que mantenha separados os valores pares e impares.
No final mostre os valores pares e impares em ordem crescente.
Entrada: 5,8,2,4,3,7,10
Saida [2,4,8,10] [3,5,7]
"""
numeros = []
par = []
impar = []
for n in range(7):
    i = int(input('Digite um número: '))
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)

numeros.append(par[:])
par.clear()
numeros[0].sort()
numeros.append(impar[:])
impar.clear()
numeros[1].sort()


print('-='*30)
print('Os valores pares digitados foram: {}'.format(numeros[0]))
print('Os valores ímpares digitados foram: {}'.format(numeros[1]))
  
        
    
    
