n = input('Digite seu nome completo: ')
n1 = n.split()
n2 = n1[0]

print('Analisando o seu nome...')
print('Seu nome em maiúsculas é {}'.format(n.upper()))
print('Seu nome me minúsculas é {}'.format(n.lower()))
print('Seu nome tem ao todo {} letras'.format(len(n)- n.count(' ')))
print('Seu primeiro nome é {} e ele tem {} letras'.format(n2, len(n2)))
