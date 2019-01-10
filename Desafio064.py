'''
Desafio064: Crie um programa que leia varios numeros inteiros pelo teclado.
O programa so vai parar quando o usuario digitar o valor 999, que é a
condição de parada. No final, mostre quantos numeros foram digitados e qual
foi a soma entre eles (desconsiderando o 999)
'''
soma = cont = 0
n = int(input('Numero: '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Numero: '))
print('\nVoce digitou {} numeros e soma entre eles é igual a {}'.format(cont, soma))
