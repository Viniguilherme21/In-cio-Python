'''
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento
'''

sal = float(input('Digite o valor de seu salários: R$'))

aumento = sal + (sal * 0.15)

print('Seu salário com 15% de aumento, ficará: R${:.2f}'.format(aumento))

