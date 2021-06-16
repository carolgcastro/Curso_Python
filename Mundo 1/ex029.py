km = int(input('Qual é a velocidade atual do carro? '))

if km > 80:
    print("""MULTADO! Você ultrapassou o limite permitido de 80km/h
    Você deve pagar uma multa de R${:.2f}!""".format((km - 80) * 7))

print('Tenha um bom dia! Dirija com segurança.')
