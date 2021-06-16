def area(l, c):
    a = l * c
    return a

l = float(input('LARGURA(m): '))
c = float(input('COMPRIMENTO(m): '))
print(f'A área de um terreno {l:.1f}x{c:.1f} é de {area(l,c)}m².')
