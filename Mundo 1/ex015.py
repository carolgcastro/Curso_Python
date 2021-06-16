km = float(input('Quantos km foram percorridos? '))

dias = int(input('Por quantos dias o carro foi alugado? '))

total = (dias * 60) + (0.15 * km)

print('O preço a pagar é de R${:.2f}'.format(total))
