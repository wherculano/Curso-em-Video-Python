# Desafio104.py
"""
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma
semelhante a função input() do Python, so que fazendo a validação para aceitar
apenas um valor numerico.
Ex: n = leiaInt('Digite um n')

n = leiaInt('Digite um numero: ')
print(f'Você acabou de digitar o numero {n}')
"""


def leiaInt(msg):
    sair = False
    valor = 0
    while True:
        num = input(msg)
        if num.isnumeric():
            valor = int(num)
            sair = True
        else:
            print('\033[0;31mERRO: Digite um NUMERO valido!\033[m')
        if sair:
            break
    return valor


# Main
n = leiaInt('Digite um numero: ')
print(f'Voce digitou o numero {n}')
