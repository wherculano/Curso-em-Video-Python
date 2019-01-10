#Desafio044

preco = float(input('\nQual o valor da compra?\nR$:'))
perc = 0
valor = 0

print('\n','-'*9,'FORMA DE PAGAMENTO','-'*9,end='')

def juros(p,j):
    taxa = p * (j/100)
    return p - taxa
    
cond_pagamento = input('''
    1- Dinheiro/Cheque
    2- A vista no cartao
    3- Em ate 2x no cartao
    4- 3x ou mais no cartao
    Opcao: ''')
       
if cond_pagamento == '1':
    perc = 10
    valor = juros(preco,perc)
    print('\nValor com 10% de desconto é R${:.2f}'.format(valor))
    
elif cond_pagamento == '2':
    perc = 5
    valor = juros(preco,perc)
    print('\nValor com 5% de desconto é R${:.2f}'.format(valor))  

elif cond_pagamento == '3':
    valor = preco / 2
    print('\nValor sera em 2x de R${:.2f}'.format(valor))  

elif cond_pagamento == '4':
    qt = int(input('\nEm quantas vezes pretende pagar?\nVezes: '))
    taxa = -20
    valor = juros(preco,taxa)
    valor /= qt
    print('\nValor sera em {}x de R${:.2f}'.format(qt,valor))  
else:
    print('\nOpção inválida!')    
