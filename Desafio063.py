'''
Desafio063: Escreva um programa que leia um numero n inteiro qualquer
e mostre na tela os n primeiros elementos de uma sequencia de Fibonacci
Ex.: 0 - 1 - 1 - 2 - 3 - 5 - 8
'''
print('-'*30)
print('SEQUÊNCIA DE FIBONACCI')
print ('-'*30)
num = int(input('Quantos números voce quer mostrar: '))
t1 = 0
t2 = 1
print ('{} -> {}'.format(t1,t2),end='')
cont = 3
while cont <= num:
    t3 = t1 + t2
    cont += 1
    t1 = t2
    t2 = t3
    print(' -> {}'.format(t3),end='')
print(' -> FIM')