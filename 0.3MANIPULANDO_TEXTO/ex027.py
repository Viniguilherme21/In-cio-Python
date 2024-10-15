'''
Faça um programa que leia o nome completo de uma pessoa e mostre o primeiro e o último nome separadamente.

Exemplo: Vinicius Guilherme dos Santos
Primeiro: Vinicius
Último: Santos
'''

nome = input('Digite seu nome completo: ').strip()

print('Muito prazer em te conhecer!')
print('Seu primeiro nome é: {}'.format(nome[:nome.find(' ')])) #ESTOU PROCURANDO AS PALAVRAS ESCRITAS DO 0 ATÉ O PRIMEIRO ESPAÇO
print('Seu último nome é: {}'.format(nome[nome.rfind(' '):])) # ESTOU PROCURANDO DA DIREITA PARA ESQUERDA ATÉ O PRIMEIRO ESPAÇO


