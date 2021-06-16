a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')

lista = [a1,a2,a3,a4]

from random import randint

num = randint(0,3)

print('O aluno escolhido foi {}'.format(lista[num]))

'''
ou
usar random.choice(lista)
'''
