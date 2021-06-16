from random import randint
from time import sleep

print("""Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?""")
guess = int(input('Qual é seu palpite? '))

cont = 1
print('PROCESSANDO...')
num = randint(0,10)
sleep(1)

while guess != num:
    if guess < num:
        print('Mais...Tente mais uma vez.')
    if guess > num:
        print('Menos...Tente mais uma vez.')
    guess = int(input('Qual é seu palpite? '))
    cont += 1
print('Acertou com {} tentativas. Parabéns!'.format(cont))

