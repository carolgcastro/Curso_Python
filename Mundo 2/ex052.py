num = int(input('Digite um número: '))
cont = 0

for x in range(1, num+1):
    if num % x == 0:
        cont += 1
if cont == 2:
    print("""O número {} foi divisível 2 vezes
E por isso ele É PRIMO""".format(num))
else:
    print("""O número {} foi divisível {} vezes
E por isso ele NÃO É PRIMO""".format(num, cont))
        
#ver aula 52 para saber das cores
