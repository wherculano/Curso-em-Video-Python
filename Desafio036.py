#Desafio036 - Aprovar emprestimo bancario

val_casa = float(input('Qual o valor da Casa que deseja comprar?\nR$: '))
val_sal = float(input('Qual o valor do seu salario?\nR$: '))
qt_anos = int(input('Em quantos anos pretende pagar a casa?\nResp.: '))

anos = qt_anos * 12
val_max = (30/100) * val_sal
val_mensal =  val_casa / anos


if val_mensal > val_max:
    print('\nO empréstimo foi negado pois R${:.2f} excede o valor permitido\
 que é de R${:.2f}!'.format(val_mensal, val_max))
else:
    print('\nO valor das prestações será de {}x de R${:.2f}'.format(anos, val_mensal))

    
