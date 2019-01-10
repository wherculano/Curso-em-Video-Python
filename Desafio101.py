#Desafio101.py
'''
Crie um programa que tenha uma função chamada voto() que vai receber
como parametro o ano de nascimento de uma pessoa, retornando um valor literal
indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
'''
def voto(nasc):
	from datetime import date
	ano_atual = date.today().year
	idade = ano_atual - nasc
	if idade < 16:
		return f'Com {idade} anos: NÃO VOTA!'
	elif 16 <= idade < 18 or idade > 65:
		return f'Com {idade} anos: VOTO OPCIONAL!'
	else:
		return f'Com {idade} anos: VOTO OBRIGATÓRIO!'
		

ano = int(input('Em que ano você nasceu?\n>>> '))
print(voto(ano))
