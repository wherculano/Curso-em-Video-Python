#--MUNDO 3--
#Desafio 77
'''
Crie um programa que tenha uma tupla com varias palavras (sem acento).
Depois mostrar para cada palavra, quais sao as suas vogais.
na palavra APRENDER temos "a e e"
'''

vogais = ('a','e','i','o','u')
palavras = ('Crie','um','programa','que','tenha',
            'uma','tupla','com','varias','palavras',
            'e','mostre','suas','vogais')

for p in palavras:
    print('\nNa palavra {} temos as vogais: '.format(p.upper()), end='')
    for vogal in p:
        if vogal.lower() in vogais:
            print(vogal, end=' ')



