matriz = [[0,0,0],[0,0,0],[0,0,0]]
spar, maior, scol = 0, 0 ,0
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]:'))
print('-='*20)
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c] #soma de pares
    print()
for l in range(3):
    scol += matriz[l][2] #soma da ultima coluna
for c in range(3):
    if c == 0 or matriz[l][c] > maior:
        maior = matriz[l][c] #maior valor segunda linha
print('-='*20)
print(f'''A soma dos valores pares é {spar}
A soma dos valores da terceira coluna é {scol}
O maior valor da segunda linha é {maior}''')
