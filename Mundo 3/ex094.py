lista = []
dici = {}
dici['nome'] = input('Nome: ')
dici['sexo'] = input('Sexo:[M/F] ')
dici['idade'] = int(input())
lista.append(dici.copy())
cont = 1

while True:
    op = input('Quer continuar? [S/N]')
    if op == 'n':
        break
    while op != 's' or op != 'n':
        print('ERRO! Por favor, digite apenas M ou F')
        op = input('Quer continuar? [S/N]')
    dici['nome'] = input('Nome: ')
    dici['sexo'] = input('Sexo:[M/F] ')
    dici['idade'] = int(input())
    lista.append(dici.copy())
    cont += 1
