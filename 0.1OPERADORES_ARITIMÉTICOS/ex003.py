'''
Crie um script Python que leia dois números e mostre a soma entre eles.
'''


#Neste caso eu tive que inserir o INT antes do INPUT.
#Caso eu NÃO colocasse o INT, a linguagem iria reconhcer o INPUT como um texto e não como número
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s =  n1+n2

"PRIMEIRA EXECUÇÃO"
print('A soma dos números è=', s)

"SEGUNDA EXECUÇÃO"
print('A some dos números é: {}'.format(s))
#Nesta execução, insemos o {}.FORMAT(). O que tiver dentro do parêntese do FORMAT será inserido no {}

"TERCEIRA EXECUÇÃO"
print('A some entre {} e {} vale {}'.format(n1, n2, s))
#Nesta execução, notamos a importância de utilizar as chaves {}. Isso torna nosso cógigo mais facíl de ser executado





