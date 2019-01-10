#Desafio24
n = input('\nCidade: ').strip()

resp1 = n[:5].upper() == 'SANTO'
resp2 = 'SANTO' in n.upper().split()

if (resp1 == True):
    resp1 = 'SIM!'
else:
    resp1 = 'NÃO!'
    
if (resp2 == True):
    resp2 = 'SIM!'
else:
    resp2 = 'NÃO!'
   
print ('\nComeça com Santo? {}'.format(resp1))
print ('Possui Santo no nome? {}'.format(resp2))