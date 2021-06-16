total = 0
maior = 0
menor = 0
c = 1
nome_m = ''

print('-'*30)
print('     LOJA SUPER BARATÃO')
print('-'*30)

while True:
    nome = input('Nome do produto: ')
    preco = float(input('Preço: R$'))
    if preco > 1000:
        maior += 1
    total += preco #soma preço de todos os produtos
    if c == 1 or preco < menor:
        menor = preco
        nome_m = nome
    c +=1
    op = input('Quer continuar? [S/N] ').upper().strip()
    if op == 'N':
        break
print('---------- FIM DO PROGRAMA -----------')
print(f"""O total da compra foi de R${total:.2f}
Temos {maior} produtos custando mais de R$1000.00
O produto mais barato foi {nome_m} que custa R${menor:.2f}""")
