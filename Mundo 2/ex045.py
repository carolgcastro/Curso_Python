from random import randint
from time import sleep
pc = randint(0,2)

print("""Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA""")
pessoa = int(input('Qual é a sua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)

itens = ('Pedra', 'Papel', 'Tesoura')
print(15 * '-=')
print ('O computador escolheu {}'.format(itens[pc]))
print ('O jogador escolheu {}'.format(itens[pessoa]))
print(15 * '-=')

if pc == 0:
    if pessoa == 0:
        print('EMPATE')
    elif pessoa == 1:
        print('JOGADOR VENCE')
    elif pessoa == 2:
        print('JOGADOR PERDE')
    else:
        print('Opção Inválida')
elif pc == 1:
    if pessoa == 1:
        print('EMPATE')
    elif pessoa == 2:
        print('JOGADOR VENCE')
    elif pessoa == 0:
        print('JOGADOR PERDE')
    else:
        print('Opção Inválida')
else:
    if pessoa == 2:
        print('EMPATE')
    elif pessoa == 0:
        print('JOGADOR VENCE')
    elif pessoa == 1:
        print('JOGADOR PERDE')
    else:
        print('Opção Inválida')
