from random import randint
print('-='*30)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*30)
v = 0

while True:
    num = int(input('Digite um valor: '))
    op = input('Par ou Ímpar? [P/I] ').upper()
    print('-'*30)
    pc = randint(0,10)
    if pc + num % 2 == 0:
        print(f'Você jogou {num} e o computador {pc}. Total de {num+pc} DEU PAR')
        if op == 'P':
            print('Você GANHOU!')
            v += 1
        if op == 'I':
            print('Você PERDEU!')
            break
    else:
        print(f'Você jogou {num} e o computador {pc}. Total de {num+pc} DEU ÍMPAR')
        print('-'*30)
        if op == 'I':
            print('Você GANHOU!')
            v += 1
        if op == 'P':
            print('Você PERDEU!')
            break       
print(f'GAME OVER! Você ganhou {v} vezes.')
