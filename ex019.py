from random import choice
n1 = input('digite um nome: ')
n2 = input('digite um nome: ')
n3 = input('digite um nome: ')
n4 = input('digite um nome: ')
lista = [n1,n2,n3,n4]

e = choice(lista)
print('O aluno escolhido foi: {}'.format(e))