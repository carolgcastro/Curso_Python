op = 's'
maior = 0
menor = 0
cont = 0
som = 0

while op == 's':
    num = int(input('Digite um número: '))
    cont += 1
    som += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor =  num
    op = input('Quer continuar? [s/n] ')
media = som / cont
print("""Você digitou {} números e a média foi {}
O maior valor foi {} e o menor foi {}""".format(cont, media, maior, menor))
