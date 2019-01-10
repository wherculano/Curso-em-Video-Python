dias = int(input('\nDias alugados com o carro: '))
km = float(input('KM rodados com o carro: '))

total = (dias * 60) + (km * 0.15)
print('O valor total a pagar é de R${:.2f}'.format(total))
