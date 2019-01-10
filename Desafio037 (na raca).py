n = int(input('Digite um numero inteiro: '))

print('\n','-'*3,'CONVERSOR','-'*3)
base = input('1- Decimal para Binário\n2- Decimal para Octal\n3- Decimal para Hexadecimal\n4- Sair\nOpção: ')

def convert(num, base):
    lista = ''
    hexa = '0123456789ABCDEF'
    quociente = num
    while True:
        resto = quociente % base
        quociente //= base
        lista += hexa[resto]
        if quociente == 0:
            break
    return lista[::-1]

if base == '1':
    base = 2
elif base == '2':
    base = 8
elif base == '3':
    base = 16
elif base == '4':
    quit()
    
else:
    print('Opção inválida!')
    
print(convert(n,base))

