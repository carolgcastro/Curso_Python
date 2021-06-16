from random import randint
from time import sleep
def sorteia():
    print('Sorteando 5 valores da lista: ', end='')
    for x in range(5):
        s_num = randint(1,10)
        print(s_num, end=' ')
        sleep(.5)
        num.append(s_num)
    print('PRONTO!')
    
def somaPar(lista):
    ac = 0
    for n in lista:
        if n % 2 == 0:
            ac += n
    return ac

num = []
sorteia()
s = somaPar(num)
print(f'Somando os valores pares de {num}, temos {s}')
