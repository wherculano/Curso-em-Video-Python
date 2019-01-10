'''
Desafio050: Leia 6 mumeros inteiros e mostre a soma apenas dos que sao pares
'''
lista = []
soma = 0
for i in range(1,7):
    num = int(input('Digite um numero: '))
    if num % 2 ==0:
        lista.append(num)
        soma += num
print('Numeros pares: {}'.format(lista))
print('Soma entre os numeros pares: {}'.format(soma))


