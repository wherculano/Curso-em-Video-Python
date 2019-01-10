#Desafio092

from datetime import datetime

dados = {}
dados['nome'] = input('Nome: ')
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('CTPS [0 se nao tiver]: '))

if dados['ctps'] != 0:
	dados['contratacao'] = int(input('Ano de Contratacao: '))
	dados['sario'] = float(input('Salario: '))
	dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - datetime.now().year)

print('=-'*20)

for k, v in dados.items():
	print(f'  - {k.upper()} tem o valor {v}')
