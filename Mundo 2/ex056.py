ac_i = 0
ac_20 = 0
maior = 0
for p in range(1,5):
    print('----- {}º PESSOA -----'.format(p))
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ')
    ac_i += idade #acumula soma das idades
    if sexo == 'F': 
        if idade < 20:
            ac_20 += 1 #acumula quem tem -20 anos
    if sexo == 'M':
        if idade > maior:
            maior = idade
            nome_m = nome #nome do homem mais velho
media = ac_i / 4
print("""A média de idade do grupo é de {:.1f} anos.
O homem mais velho tem {} anos e se chama {}.
Ao todo são {} mulheres com menos de 20 anos.""".format(media, maior, nome_m, ac_20))

