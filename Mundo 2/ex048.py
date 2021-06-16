ac = 0
cont = 0
for x in range(1,501,2):
    if x % 3 == 0:
        ac += x
        cont += 1
print('A soma de todos os {} valores solicitados é {}'.format(cont, ac))
