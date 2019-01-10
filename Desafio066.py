'''
Desafio66 - Crie um programa que leia varios numeros inteiros pelo teclado.
O programa so vai parar quando o usuario digitar o valor 999, que é a
condição de parada. No final, mostre quantos numeros foram digitados
e qual foi a soma entre eles (desconsiderando a flag 999)
'''
soma = cont = 0
while True:
    n = int(input('Digite um valor (999 para sair): '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'Você digitou {cont} numeros e a soma entre eles é {soma}')

