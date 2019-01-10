from random import shuffle

n1 = input ('\nNome: ')
n2 = input ('Nome: ')
n3 = input ('Nome: ')
n4 = input ('Nome: ')

print ('\n')

lista = [n1,n2,n3,n4]
print(lista)

shuffle(lista)
print(lista)