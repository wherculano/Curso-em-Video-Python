import os
os.system('clear')

print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)

val = int(input('Qual valor deseja sacar? R$'))

ced = [100,50,20,10,5,2,1]

for i in range(len(ced)):
    sac = val // ced[i]
    val %= ced[i]
    if sac == 0:
        continue
    else:
        print('{} nota(s) de {}'.format(sac,ced[i]))

print('='*30)
print('Obrigado e volte sempre!')




