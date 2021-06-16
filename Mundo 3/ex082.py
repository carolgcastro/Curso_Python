lista = []
par, imp = [], []
num = int(input('Digite um valor: '))
while True:
    lista.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        imp.append(num)
    n = input('Deseja continuar? [S/N] ')
    if 'n' == n:
        break
    num = int(input('Digite um valor: '))
print('-='*20)
print(f'''A lista completa é {lista}
A lista de pares é {par}
A lista de ímpares é {imp}''')
