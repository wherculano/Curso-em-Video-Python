"""
Desafio048: Calcule a soma de todos os numeros impares que sao multiplos de 3
e que se encontram no intervalo de 1 ate 500
"""
lista = []
soma = 0
for i in range(1,500):
    if i%3 == 0:
        lista.append(i)
        soma += i
print('Os numeros multimos de 3 são:\n{}\nE a soma entre eles é:{}'.format(lista, soma))



