frase = input('Digite uma frase: ').strip().upper().split()
junto = ''.join(frase)
inverso = ''
for x in range(len(junto)-1, -1, -1):
    inverso += junto[x]

print('O inverso de {} é {}'.format(junto, inverso))
if junto == inverso:
    print('Temos um palíndromo')
else:
    print('A frase digitada não é um palíndromo')


