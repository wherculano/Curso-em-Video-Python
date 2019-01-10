'''
Desafio049: Refazer o exercicio 9 de um numero que o usuario escolher, so que
agora utilizando um laco FOR
'''
num = int(input('Digite um numero para saber a tabuada: '))
for i in range(0,11):
    print('{} * {:02.0f} = {:02.0f}'.format(num,i,num*i))
