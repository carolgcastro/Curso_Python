termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = termo + (10 - 1) * razao
cont = 0

while termo <= decimo:
    print(termo, end = ' → ')
    termo += razao
    cont += 1
print('PAUSA')

op = 1

while op != 0:
    c = 1
    op = int(input('Quantos termos você quer mostrar a mais? '))
    while c <= op:
        print(termo, end = ' → ')
        termo += razao
        c += 1
        cont += 1
print('Profressão finalizada com {} termos mostrados.'.format(cont))
