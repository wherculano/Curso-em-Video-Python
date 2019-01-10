#Desafio34 - aumento do salario
sal = float(input('Salário: R$'))

if sal > 1250:
    aum = sal * (1+0.1)
    print('Com aumento de 10% seu novo salário é de R${:.2f}'.format(aum))
else:
    aum = sal * (1+0.15)
    print('Com aumento de 15% seu novo salário é de R${:.2f}'.format(aum))
