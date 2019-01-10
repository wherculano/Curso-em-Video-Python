"""
Desafio084 - Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final mostre:
A)Quantas pessoas foram cadastradas
B)Uma listagem com as pessoas mais pesadas
C)Uma listagem com as pessoas mais leves
Usando o 'Quer continuar após cadastrar a pessoa'
"""

pessoas = []
dados = []
leve = pesado = 0
while True:
    dados.append(input('Nome: '))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        leve = pesado = dados[1]
    elif dados[1] > pesado:
        pesado = dados[1]
    elif dados[1] < leve:
        leve = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    op = input('Deseja continuar? [S/N]: ').upper()
    if op == 'N':
        break
print('-='*30)
print(f'Há {len(pessoas)} cadastradas!')
print(f'O menor peso foi de {leve}Kg ',end='')
for pessoa in pessoas:
    if pessoa[1] == leve:
        print(f'[{pessoa[0]}]', end='')
print(f'\nO maior peso foi de {pesado}Kg ',end='')
for pessoa in pessoas:
    if pessoa[1] == pesado:
        print(f'[{pessoa[0]}]', end='')

