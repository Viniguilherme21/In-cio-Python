'''
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR
'''

num = int(input('Digite um número inteiro: '))
cont = num % 2
if cont == 0:
    print('O número {} é \033[1;36mPAR \033[m'.format(num))
else:
    print('O número {} é \033[1;31mÍMPAR \033[m'.format(num))
