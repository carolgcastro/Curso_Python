from random import randint
from time import sleep
n = int(input('Quantos jogos você quer que eu sorteie?  '))
print(f'-=-=-=-= SORTEANDO {n} JOGOS -=-=-=-=')
for s in range(n):
    num_l = []
    for x in range(6):
        num = randint(1,60)
        num_l.append(num)
        num_l.sort
    print(f'Jogo {s+1}: {num_l}')
    sleep(1)
