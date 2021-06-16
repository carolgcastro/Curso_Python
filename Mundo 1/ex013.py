salario = float(input('Digite seu salário atual: R$'))

aumento = salario + (salario * 0.15)

print('Seu salário de R${}, com 15% de aumento passa a ser R${:.2f}'.format(salario, aumento))
