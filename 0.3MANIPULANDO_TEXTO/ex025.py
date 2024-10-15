'''
Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
'''

nome = input('Digite seu nome: ').strip().upper()

if 'SILVA' in nome:
    print('Seu nome CONTÉM o nome SILVA')
else:
    print('Seu nome NÃO contem o nome SILVA')

