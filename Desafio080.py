#Desafio080
'''
Digitar 5 valores numericos e cadastra-los em uma lista,
ja na posição certa sem usar o sort().
No final, mostrar a lista ordenada.

'''

lista = []
for i in range(5):
    valor = int(input('Digite um valor: '))
    if len(lista) == 0 or valor > lista[-1]:
        lista.append(valor)
        print('Adicionado ao final da lista!')
    else:
        for x in range(len(lista)+1):
            if valor <= lista[x]:
                lista.insert(x,valor)
                break
        print('Adicionado na posição {} da lista'.format(lista.index(valor)))
        
print('-='*30)   
print('Os valores digitados em ordem foram {}'.format(lista))
