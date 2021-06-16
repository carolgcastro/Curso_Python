print('Analisador de Triângulos')
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

tri = ''
if a + b > c and a + c > b and b + c > a:
    if a == b and b == c:
        tri = 'EQUILÁTERO'
    elif a == b or a == c or b == c:
        tri = 'ISÓSCELES'
    else:
        tri = 'ESCALENO'
    print('Os segmentos acima PODEM FORMAR um triângulo {}!'.format(tri))
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')
