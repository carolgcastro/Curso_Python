lista = []
num = int(input('Digite um valor: '))
while True:
    lista.append(num)
    n = input('Deseja continuar? [S/N] ')
    if 'n' == n:
        break
    num = int(input('Digite um valor: '))
lista.sort(reverse=True)
print('-='*20)
if 5 in lista:
    print(f'''Você digitou {len(lista)} elementos.
Os valores em ordem decrescente são {lista}
O valor 5 faz parte da lista!''')
else:
    print(f'''Você digitou {len(lista)} elementos.
Os valores em ordem decrescente são {lista}
O valor 5 não faz parte da lista!''')


