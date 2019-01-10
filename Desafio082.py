#Desafio082
'''
Leia varios numeros e coloque-os em uma lista.
Depois disso crie duas listas extras que vão conter apenas
os valores pares e os valores impares digitados respectivamente.
Ao final, mostre o conteudo das 3 listas geradas.

Digite um numero:
Quer continuar? [S/N] ->
6,2,7,8,3,9

A lista completa é
A lista de pares é
A lista de impares é


'''
lista, par, impar = [], [], []

while True:
    valor = int(input('Digite um numero: '))
    lista.append(valor)
    op = input('Quer continuar? [S/N] -> ').upper()
    if op != 'S':
        break
    
for i in range(len(lista)):
    if lista[i] % 2 == 0:
        par.append(lista[i])
    else:
        impar.append(lista[i])
        
print('-='*30)
print('A lista completa é {}'.format(lista))
print('A lista de pares é {}'.format(par))
print('A lista de impares é {}'.format(impar))




