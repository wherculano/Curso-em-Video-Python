#aumento em 15% no salario

sal = float(input('\nDigite seu salario: R$'))
nsal = sal * (1+(15/100))
#nsal = sal + (sal * 15 / 100)
print('Com aumento de 15%\nseu novo salário é de R${:.2f}'.format(nsal))

