'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado
'''

valor_casa = float(input('Digite o valor da casa R$:  '))
salario = float(input('Digite seu sálario mensal R$: '))
parcela = int(input('Em quantos anos pretende parcelar: '))
prestacao = valor_casa / (parcela * 12)
limite = salario * 0.30

print('Para pagar uma casa de R${} em 7 anos a será de R${:.2f}.'.format(valor_casa, prestacao))

if prestacao > limite:
    print('\033[1:31mEMPRÉSTIMO NEGADO\033[m')
else:
    print('\033[1:32mEMPRÉSTIMO APROVADO \033[m')

