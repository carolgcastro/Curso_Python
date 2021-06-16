print('Vou pensar em um número entr 0 e 5. Tente adivinhar!')
guess = int(input('Em que número eu pensei? '))

from random import randint
from time import sleep

print('PROCESSANDO...')

num = randint(0,5)
sleep(3)
if guess == num:
    print('PARABÉNS! Você conseguiu me vencer.')
else:
    print('GANHEI! Pensei no número {}, não no {}'.format(num, guess))
