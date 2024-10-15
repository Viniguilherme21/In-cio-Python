'''
Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e antecessor.
'''

a = int(input('Digite um valor: '))
b = a + 1
c = a - 1

print('Valor digitado: {}. O antecessor do valor digitado é {}, e o sucessor é {}'.format(a,c,b))


#RESPOSTA DO PROFESSOR
b = int(input('Digite outro valor: '))
print('Analisando o valor{}, seu antecessor é {} e o sucessor é {}'.format(b, (b-1), (b+1)))
#Desta forma nos utilizamos apenas uma variável

