"""
Faca um mini-sistema que utilize o interactive help do Python.
O usuario vai digitar o comando e o manual vai aparecer.
Quando o usuario digitar a palavra FIM, o programa se encerrará.
Obs.: Utilizar cores.


Ex.:
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~
      Sistema de Ajuda PyHelp
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Funcao ou Biblioteca -> len
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Acessando o Manual do Comando: 'len'
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Help on built-in function len in module builtins:
    len(obj, /)
        Return the number of items in a container
"""
from time import sleep


def pyHelp(com):
    msgFormatada(f"Acessando o Manual do Comando: '{com}'", 4)
    print(cores[6], end="")
    help(com)
    print(cores[0], end="")
    sleep(2)


def msgFormatada(msg, cor=0):
    tam = len(msg) + 4
    print(cores[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(cores[0], end='')
    sleep(1)


cores = ('\033[m',         # 0 - sem cor
         '\033[0;30;41m',  # 1 - vermelho
         '\033[0;30;42m',  # 2 - verde
         '\033[0;30;43m',  # 3 - amarelo
         '\033[0;30;44m',  # 4 - azul
         '\033[0;30;45m',  # 5 - roxo
         '\033[7;30m',     # 6 - branco
         )

if __name__ == '__main__':
    command = ''
    while True:
        msgFormatada('SISTEMA DE AJUDA PyHELP', 2)
        command = input('Funcao ou Biblioteca -> ')
        if command.upper() == 'FIM':
            break
        else:
            pyHelp(command)
    msgFormatada('ATÉ LOGO', 1)
