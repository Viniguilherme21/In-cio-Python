'''
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
'''


a = int(input('Digite um valor: '))
b = a * 2
c = a * 3
d = a ** (1/2)

print('Valor digitado: {}. \n O dobro do valor é {} \n O triplo é {} \n A raiz quadrada é {:.2f}.'.format(a, b, c, d) )

#OUTRA POSSIBILIDADE
e = int(input('Digite outro valor: '))
print('Valor digitado: {}\n> Dobro do valor: {} \n> Triplo do valor: {} \n> Raiz quadrada do valor: {:.2f}'.format(e, (e*2), (e*3), (e**(1/2))))

