'''
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
Exemplo: Digite um número:1837
Unidade: 7
Dezena: 3
Centena:8
Milhar: 1
'''

num = int(input('Escreva um número de 0 a 9999: '))
m = num // 1000 % 10
c = num // 100 % 10
d = num // 10 % 10
u = num // 1 % 10

print('Milhar: {}'.format(m))
print('Centena: {}'.format(c))
print('Dezena: {}'.format(d))
print('Unidade: {}'.format(u))






