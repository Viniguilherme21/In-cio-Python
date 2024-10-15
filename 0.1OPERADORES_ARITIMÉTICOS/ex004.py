'''
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo
primitivo e todos as informações possiveis sobre ela.
'''


a = input('Digite um algo: ') #O (a) é o objeto.
print('O tipo primitivo deste valor é', type(a))
print('Só tem espaços? ', a.isspace()) #ISSPACE verificando se só tem espaço
print('É um número? ', a.isnumeric()) #ISNUMERIC verificando se é um número
print('É alfabético? ', a.isalpha()) #ISAPLHA verificandp se é alfabético
print('É alfanumérico? ', a.isalnum()) #ISALNUM verificando se tem letras e números
print('Está em maiúscula? ', a.isupper()) #ISUPPER Verificando se está TUDO em maiúscula
print('Está em minúscula? ', a.islower()) #ISLOWER Verificando se está TUDO em minúscula
print('Está capitalizada?', a.istitle()) # ISTITLE verificando se a primeira letra é maiúscula



