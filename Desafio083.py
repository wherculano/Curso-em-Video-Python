###Desafio083
##'''
##Crie um programa onde o usuario digite um expressão (matematica) qualquer que use parenteses.
##Seu aplicativo deverá analisar se a expressão passada está com os parenteses
##abertos e fechados na ordem correta.
##
##Digite a expressão: ((a+b)*c)
##Sua expressão é válida!
##Digite a expressão: ((a+b)*c))
##Sua expressão está errada!
##Digite a expressão: ((a+b)*(a*c)-2)
##Sua expressão está errada!
##'''
##Minha solução
##exp = input('Digite um expressão: ')
##char = []
##for i in range(len(exp)):
##    if exp.count('(') == exp.count(')'):
##        if exp[0] == '(' and exp[-1] == ')':
##            print('Sua expressão é válida!')
##        else:
##            print('Os parenteses não estão abertos/fechados corretamente!')
##        break
##    else:
##        print('Sua expressão está errada!')
##        break
##Do Guanabara
exp = input('Digite a expressão: ')
par = []
for simb in exp:
    if simb == '(':
        par.append('(')
    elif simb == ')':
        if len(par) > 0:
            par.pop()
        else:
            par.append(')')
            break
if len(par) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão é inválida!')
