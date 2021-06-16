lista = list(input('Informe um número: '))

print('Analisando o número {}'.format(''.join(lista)))

i = 0
while len(lista) < 4:
    lista[0] = 0
    i += 1
    
print('Unidade: {}'.format(lista[3]))
print('Dezena: {}'.format(lista[2]))
print('Centena: {}'.format(lista[1]))
print('Milhar: {}'.format(lista[0]))
          
