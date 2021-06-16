par, imp = [], []
for t in range(7):
    num = int(input(f'Digite o {t+1}º valor: '))
    if num % 2 == 0:
        par.append(num)
    else:
        imp.append(num)
par.sort()
imp.sort()
print(f'''Os valores pares digitados foram: {par}
Os valores ímpares digitados foram: {imp}''')
'''feito com mais listas que pedido no enunciado'''
