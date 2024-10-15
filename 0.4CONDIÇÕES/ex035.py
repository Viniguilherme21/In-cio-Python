'''
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triândulo
'''

print('-=' * 20)
print('\033[1;36mANALISADOR DE TRIÂNGULOS\033[m')
print('-=' * 20)
r1 = float(input('Digite o valor da reta1: '))
r2 = float(input('Digite o valor da reta2: '))
r3 = float(input('Digite o valor da reta3: '))

if (r2 + r3) > r1 and (r1 + r3) > r2 and (r1 + r2) > r3:
    print('\033[1;31mPodemos\033[m formar um triângulo!')
else:
    print('\033[1;31mNão podemos\033[m formar um triângulo!')
