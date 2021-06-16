nome = input('Nome: ')
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
lista = []
while True:
    media = (n1+n2)/2
    pessoa = ([nome, [n1, n2], media])
    lista.append(pessoa)
    s = input('Deseja continuar? [S/N] ')
    if s == 'n':
        break
    nome = input('Nome: ')
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
print('-='*20)
for i, x in enumerate(lista):
    print(f'{i:<4}{lista[i][0]:<10}{lista[i][2]:.1f}')
while True:
   op = int(input('Mostrar notas de qual aluno? '))
   if op == 999:
       break
   print(f'Notas de {lista[op][0]} são {lista[op][1]}') 
