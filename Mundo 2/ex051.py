termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = termo + (10 - 1) * razao

for x in range(termo, decimo+1, razao):
        print(x, end = ' → ')
print('ACABOU')
