#Desafio26
frase = input ('\nDigite uma frase: ').strip()

cont = frase.upper().count('A')
print ('Quantidade: {}'.format(cont))

pos = frase.upper().find('A')
print('Primeira Posição: [{}]'.format(pos))

ult = frase.upper().rfind('A')
print('Última Posição: [{}]'.format(ult))


