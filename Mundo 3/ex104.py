def leiaInt(n):
    num = input(n)
    if num.isnumeric():
        return num
    else:
        while not num.isnumeric():
            print('ERRO! Digite um número inteiro válido.')
            num = input(n)
        return num

res = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {res}')
