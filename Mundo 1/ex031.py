dist = float(input('Qual é a distância da sua viagem? '))

if dist > 200:
    total = dist * 0.45
    print("""Você está prestes a começar sua viagem de {}Km
    E o preço da sua passagem será de R${:.2f}""".format(dist, total))
else:
    total = dist * 0.50
    print("""Você está prestes a começar sua viagem de {}Km
    E o preço da sua passagem será de R${:.2f}""".format(dist, total))
'''
ou
fazer da forma simplificada
'''
