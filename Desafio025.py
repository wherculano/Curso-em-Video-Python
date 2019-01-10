#Desafio25
nome = input ('\nNome: ').strip()
n = nome.upper()

sn = 'SILVA' in n

if (sn == True):
    resp = 'Sim!'
else:
    resp = 'Nao!'

print ('possui SILVA no nome? {}'.format(resp))