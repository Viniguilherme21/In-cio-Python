'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas
O nome com todas as letras minúscula
Quantas letras ao todo, sem considerar o espaço
Quantas letras tem o primeiro nome
'''


nome = input('Digite seu nome completo: ').strip() #STRIP ELIMINA OS ESPAÇOS ANTES E DEPOIS

print('Analisando seu nome:')
print('Seu nome em Maiúscula: {}'.format(nome.upper()))
print('Seu nome em Minúscula: {}'.format(nome.lower()))
print('Ao todo, seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
separa = nome.split()

print('Seu primeiro nome tem {} letras'.format(len(separa [0])))













