"""
Desafio086 - Crie um programa que crie uma matriz de dimensão 3x3 e preencha
com valores lidos pelo teclado. No final mostre a matriz com a formatação correta.
Entrada: 1,2,3,4,5,6,7,8,9
Saida [1][2][3].....[7][8][9]
"""


lista = [list(map(int, [input(f'[{linha}][{coluna}]: ') for coluna in range(0,3)])) for linha in range(0,3)]
print('-='*30)
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{lista[linha][coluna]:^5}]',end='')
    print()

###Guanabara
##matriz = [[0,0,0],[0,0,0],[0,0,0]]
###Alimentando a Matriz
##for linha in range(0,3):
##    for coluna in range(0,3):
##        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha},{coluna}]: '))
##
##print('-='*30)
###Mostrando a Estrutura
##for linha in range(0,3):
##    for coluna in range(0,3):
##        print(f'[{matriz[linha][coluna]:^5}]',end='')
##    print()
