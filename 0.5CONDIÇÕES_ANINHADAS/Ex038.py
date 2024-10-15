'''
Ecreva um programa que leia dois números inteiros e compare-os,
mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
'''

num1 = int(input('Digite o primeiro valor inteiro: '))
num2 = int(input('Digite o segundo valor inteiro: '))

if num1 > num2:
    print('O\033[1:33m PRIMEIRO\033[m valor é \033[1:33mMAIOR \033[m')
elif num2 > num1:
    print('O\033[1:31m SEGUNDO\033[:m valor é \033[1:31mMAIOR \033[m')
else:
    print('Não existe valor maior\033[1:34m OS DOIS SÃO IGUAIS\033[m')

