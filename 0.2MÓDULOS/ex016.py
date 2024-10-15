'''
Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.

Exemplo: Digite um número: 6.127
O número 6.127 tem a parte inteira 6.
'''

from math import trunc
num = float(input('Digite um número real inteiro: '))
print('O número arredondado para cima é igual a:  {}'.format(trunc(num)))

#A FUNÇÃO TRUNC ELIMINA O QUE VEM APÓS O PONTO, DO NÚMERO DIGITADO.






