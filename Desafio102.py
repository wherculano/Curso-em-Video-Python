#Desafio102.py
'''
Crie um programa que tenha uma função fatorial() que recebe dois parametros:
o primeiro que indique o numero a calcular e o outro chamado show,
que será um valor lógico (opcional) indicando se será mostrado ou não na
tela o processo de calculo do fatorial

print(fatorial(5))
>>> 120

print(fatorial(5, True))
>>> 5 x 4 x 3 x 2 x 1 = 120
'''

def fatorial(n, show=False):
    '''
    Calcula o Fatorial de um numero
    :param n: o numero a ser calculado
    :param show: (opcional) Mostrar ou nao a conta
    '''
    f = 1
    for c in range(n,0,-1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ',end='')
            else:
                print(' = ',end='')
        f *= c
    return f


help(fatorial)
print(fatorial(5))
print(fatorial(5, True))
