#Desafio095
time = list()
partidas = list()
jogador = dict()
while True:
	jogador.clear()
	partidas.clear()
	jogador['nome'] = input('Nome do jogador: ').title()
	tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
	for c in range(0, tot):
		partidas.append(int(input(f' Quantos gols na partida {c+1}: ')))
	jogador['gols'] = partidas[:]
	jogador['tot'] = sum(partidas)
	time.append(jogador.copy())
	while True:
		resp = input('Quer continuar? [S/N]: ').upper()[0]
		if resp in 'SN':
			break
		else:
			print('ERRO! Digite apenas S ou N!\n')
	if resp == 'N':
		break
print('-='*20)
print('cod ',end='')
for i in jogador.keys():
	print(f'{i:<15} ',end='')
print()
print('-='*20)
for k, v in enumerate(time):
	print(f'{k:>3} ',end='')
	for d in v.values():
		print(f'{str(d):<15} ',end='')
	print()
print()
while True:
	busca = int(input('Mostrar dados de qual jogador? (999 para sair): '))
	if busca == 999:
		break
	if busca >= len(time):
		print(f'\nERRO! Não existe jogador com o código {busca}!')
	else:
		print(f' --LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}: ')
		for i, g in enumerate(time[busca]["gols"]):
			print(f'  No jogo {i+1} fez {g} gols!')
	print()
print(' FIM '.center(20,'-'))
	

