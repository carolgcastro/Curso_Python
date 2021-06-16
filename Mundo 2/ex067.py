while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*30)
    if num < 0:
        break
    x = 1
    while x <= 10:
        print(f'{num} x { x } = {num*x}')
        x += 1
    print('-'*30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
