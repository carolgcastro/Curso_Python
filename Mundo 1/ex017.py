co = float(input('Qual é o tamanho do cateto oposto? '))
ca = float(input('Qual é o tamanho do cateto adjascente? '))

from math import hypot

hip = hypot(co,ca)

print('A hipotenusa vai medir {:.2f}'.format(hip))
