'''
Escreva um programa que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão:
- 1 para BINÁRIO
-2 para OCTAL
-3 para HEXADECIMAL
'''

num = int(input('Digite um número inteiro: '))
print('''Escolha a base para conversão:')
[1] conversão para BINÁRIO')
[2] conversão para OCTAL')
[3] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))


if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIAMAL é igual a {}'.format(num, hex(num)[2:]))
else: print('''A opção digitada deve ser 1 2 ou 3 
== \033[1:31m digite a opção correta \033[m ==''')

