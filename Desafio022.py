#Desafio 22
n = input ('\nNome: ').strip() #ja exclui os espacos desnecessários

print ('\nMaiusculas: {}'.format(n.upper()))
print ('Minusculas: {}'.format(n.lower()))

qt = len(n) - n.count(' ')
print('Total de letras: {}'.format(qt))

pnome = n.split()
print('Primeiro nome possui {} letras'.format(len(pnome[0])))