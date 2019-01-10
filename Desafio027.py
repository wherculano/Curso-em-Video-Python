#Desafio027
nome = input('\nNome: ').strip()
palavras = nome.split()
print('Primeiro: {}'.format(palavras[0]))
ult = len(palavras) - 1
print('Último: {}'.format(palavras[ult]))