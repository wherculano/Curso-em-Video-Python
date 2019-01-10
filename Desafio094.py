#Desafio094
pessoa = dict()
galera = list()
soma = med = 0

while True:
	pessoa.clear()
	pessoa['nome'] = input('\nNome: ').title()
	
	while True:
		pessoa['sexo'] = input('Sexo [M/F]: ').upper()[0]
		if pessoa['sexo'] in 'MF':
			break
		print('Digite apenas M ou F !\n')
	
	while True:
		try:
			pessoa['idade'] = int(input('Idade: '))
			break
		except:
			print('Digite uma idade válida!\n')

	soma += pessoa['idade']		
	galera.append(pessoa.copy())
	
	while True:
		resp = input('\nQuer continuar?\n[S/N]: ').upper()[0]
		if resp in 'SN':
			break
		print('Digite apenas S ou N!\n')
	
	if resp == 'N':
		break

print('-='*20)		
print(f'\nAo todo temos {len(galera)} pessoas cadastradas!')

med  = soma / len(galera)
print(f'A media de idade é de {med:5.2f} anos.')

print('As mulheres cadastradas sao ',end='')
for p in galera:
	if p['sexo'] == 'F':
		print(f'{p["nome"]}, ',end='')
print()

print('Pessoas com idade acima da media: ')
for p in galera:
	if p['idade'] >= med:
		for k, v in p.items():
			print(f' {k} = {v} ', end='')
		print()
		
print('Fim'.center(20,'='))