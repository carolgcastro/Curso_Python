from datetime import date
p = 0
maior = 0
menor = 0
for x in range(0,7):
    p += 1
    ano = int(input('Em que ano a {}º pessoa nasceu? '.format(p)))
    idade = date.today().year - ano
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print("""Ao todo tivemos {} pessoas maiores de idade
E também tivemos {} pessoas menores de idade""".format(maior, menor))
