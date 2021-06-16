from random import randint
from operator import itemgetter
from time import sleep
dici = dict()
for x in range(1,5):
    dici[x] = randint(1,6)
ranking = dict()
for k,v in dici.items():
    print(f'jogador{k} tirou {v} no dado.')
    sleep(1)
print('-='*20)
ranking = sorted(dici.items(), key=itemgetter(1), reverse=True)
for i,v in enumerate(ranking):
    print(f'{i+1}º lugar: jogador{v[0]} com {v[1]}')
    sleep(1)
