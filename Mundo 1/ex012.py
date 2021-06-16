preco = float(input('Qual o preço do produto? R$'))

promo = preco * 0.05

total = preco - promo

print('Seu produto com 5% off = R${:.2f}'.format(total))

'''
ou

total = preco - (preco * 5 / 100)
'''
