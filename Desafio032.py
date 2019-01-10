#Desafio32 - Verificar se é bissexto

# Quais as condições para que seja bissexto?
# De 4 em 4 anos é de 400 em 400 anos é bissexto.
# De 100 em 100 anos não é ano bissexto.

from datetime import date
ano = int(input('Digite um ano qualquer ou 0 para analisar o ano atual: '))
if ano == 0:
        ano = date.today().year #pega o ano atual do PC
        
if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):
	print('O ano {} É bissexto'.format(ano))
else:
	print('O ano {} NÃO É bissexto'.format(ano))



