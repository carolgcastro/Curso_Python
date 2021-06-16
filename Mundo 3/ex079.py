lista = []
while True:
    num = int(input('Digite um valor: '))
    if num in lista:
        print('Valor duplicado! Não vou adicionar...')
    else:
        lista.append(num)
        print('Valor adicionado com sucesso!')
    op = input('Quer continuar? [S/N] ').upper()
    if op == 'N':
        break
print('-='*30)
lista.sort()
print(f'Você digitou os valores {lista}')
