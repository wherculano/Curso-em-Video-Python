#Desafio090
aluno = dict()
aluno['nome'] = input('Nome: ')
aluno['media'] = float(input('Media de {}: '.format(aluno['nome'])))

print("~="*30)

if aluno["media"] < 5:
	aluno['situac'] = 'Reprovado'
elif aluno["media"] >= 5 and aluno["media"] < 7:
	aluno['situac']	= 'Recuperacao'
else:
	aluno['situac']= 'Aprovado'

for k, v in aluno.items():
	print('  - {} é igual a {}'.format(k,v))
	