#Desafio081
'''
Ler varios numeros e colocar em uma lista.
Depois mostre:
A) Quantos numeros foram digitados
B) A lista de valores ordenada de forma decrescente
C) Se o valor 5 foi digitado e está ou não na lista.
'''

lista = []
while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    op = input('Quer continuar? [S/N] -> ').upper()
    if op != 'S':
        break
print('-='*30)
print('Voce digitou {} elementos'.format(len(lista)))

lista.sort(reverse=True)
print('Os valores em ordem Decrescente são {}'.format(lista))

if 5 in lista:
    print('O valor 5 faz parte da lista e está na posição {}'.format(lista.index(5)))
else:
    print('O valor 5 não foi encontrado na lista')


        

