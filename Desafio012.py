#calculo de produto com 5% de desconto 

val = float(input('\nDigite o valor do produto: R$'))
nval = val * (1 - (5 / 100))
#nval = val - (val * 5 / 100)

print ('Com 5% de desconto o valor é de R${:.2f}'.format(nval))