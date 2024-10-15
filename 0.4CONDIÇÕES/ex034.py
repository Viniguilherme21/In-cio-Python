'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.

Para salários superiores a R$1.250 ,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%
'''

sal = float(input('Qual valor de seu salário: R$'))

if sal > 1250:
    print('Você recebeu um aumento de 10% \n=== Seu novo salário é de R$: {} ==='.format((sal * 0.10) + sal))
else:
    print('Você recebeu um salário de 15% \n=== Seu novo salário é de R$ {} ==='.format((sal * 0.15) + sal))

