'''Desafio059: Crie um programa que leia 2 valores e mostre um menu na tela.
[1]Somar [2]Multiplicar [3]Maior [4]Novos numeros [5]Sair
Seu programa devera realizar a operação solicitada em cada caso'''

op = ''
stop = False

n1 = int(input('Type an integer number: '))
n2 = int(input('Type another one: '))

while not stop:
    op = int(input('''\n-----MENU-----
[1] Sum
[2] Multiply
[3] Greater or Lesser
[4] New numbers
[5] Exit
Option: '''))
    if op == 1:
        print('\t{}+{}={}'.format(n1, n2,(n1+n2)))
    elif op == 2:
        print('\t{}x{}={}'.format(n1,n2,(n1*n2)))
    elif op == 3:
        if n1 > n2:
            print('\t{} > {}'.format(n1,n2))
        elif n1 < n2:
            print('\t{} < {}'.format(n1,n2))
        else:
            print('\t{} = {}'.format(n1,n2))
    elif op == 4:
        n1 = int(input('Type an integer number: '))
        n2 = int(input('Type another one: '))
    elif op == 5:
        print('Exit...')
        stop = True
    else:
        print('Invalid option')
