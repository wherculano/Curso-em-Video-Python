#--MUNDO 3--
#Desafio 73
'''
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Brasileirão, na ordem de colocação. Depois mostre:
A) Apenas os 5 primeiros colocados.
B) Os últimos 4 colocados
C) Uma lista com os times em Ordem Alfabetica
D) Em que posição na tabela está o time da Chapecoense.
'''

times = ('Atletico-MG','Flamengo','Corinthians','Palmeiras','Fluminense','America-MG','São Paulo','Grêmio','Vasco','Botafogo',
         'Sport Recife','Cruzeiro','Vitória','Santos','Chapecoense','Atlético-PR','Internacional','Bahia','Ceará','Paraná')

#A)e
print('\nOs cinco primeiros colocados são:')
##for pos, cinco in enumerate(times[:5]):
##    print('{}º {}'.format(pos+1,cinco))
for pos, cinco in enumerate(times):
    if pos <= 4:
        print('{}º {}'.format(pos+1,cinco))

#B)
print('\nOs últimos 4 colocados são:')
for z4 in range(16,20):
    print('{}º {}'.format(z4+1, times[z4]))


#C)
print('\nOrdem Alfabética:')
print(sorted(times))

#D)
print('\nA Chapecoense está em {}º colocado.'.format(times.index('Chapecoense')+1))
