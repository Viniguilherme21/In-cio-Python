'''
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
'''

n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
n3 = float(input('Digite o terceiro valor: '))

#VERIFICANDO O MENOR VALOR
if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n1:
    menor = n3

#VERIFICANDO O MENOR VALOR
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and  n3 > n2:
    maior = n3

print('O maior valor foi o {}'.format(maior))
print('O menor valor foi o {}'.format(menor))

