#from math import factorial
num = int(input('Digite um número para calcular seu fatorial: '))
c = num
fact = 1
print('Calculando {}!'.format(num))
while c > 0:
    fact *= c
    print('{}'.format(c), end = '')
    print(' x ' if c > 1 else ' = ', end = '')
    c -= 1
print('{}'.format(fact))    
#f = factorial(num)
