ac = 0
cont = 0
for x in range(0,6):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        ac += num
        cont += 1
print('Você informou {} números PARES e a soma deles foi {}'.format(cont, ac))
