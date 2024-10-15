'''
Refaça o desafio 035 dos triângulos.
Acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: Todos os lador iguais
- ISÓSCELAS: Dois lados iguais
- ESCALENO Todas os lados diferentes
'''

print('-=' * 20)
print('\033[1;36mANALISADOR DE TRIÂNGULOS\033[m')
print('-=' * 20)
r1 = float(input('Digite o valor da reta1: '))
r2 = float(input('Digite o valor da reta2: '))
r3 = float(input('Digite o valor da reta3: '))

if (r2 + r3) > r1 and (r1 + r3) > r2 and (r1 + r2) > r3:
    print('\033[1;31mPodemos\033[m formar um triângulo!', end='')
    if r1 == r2 == r3:
        print(' Do tipo:\033[1:31m EQUILÁTERO')
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print(' Do tipo:\033[1:31mISÓSCELAS')
    else: print(' Do tipo:\033[1:31m ESCALENO')
else:
    print('\033[1;31mNão podemos\033[m formar um triângulo!')

