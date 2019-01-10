#--MUNDO 3--
#Desafio 75
'''
Desenvolva um programa que leia 4 valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A)Quantas vezes apareceu o valor 9
B)Em que posição foi digitado o primeiro valor 3
C)Quais foram os numeros pares
Se buscar valor que não existe, tem que dar erro!
    o valor 9 apareceu 0 vezes - O valor 3 nao foi digitado em nenhuma posicao (apareceu na x posicao).
'''
num = tuple(int(input('Digite o {}º numero: '.format(i+1))) for i in range(4))
print('\nVocê digitou os valores: {}'.format(num))

print('O valor 9 apareceu {} vezes.'.format(num.count(9)))

if num.count(3):
    print('O valor 3 apareceu na {}ª posição'.format(num.index(3)+1))
else:
    print('O valor 3 não foi digitado em nenhuma posição!')
    
print('Os valores pares digitados foram: ',end='')
for par in num:
    if par % 2 == 0:
        print(par, end=' ')
 

