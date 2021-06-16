info = input('Informe seu sexo [F/M]: ')

while info not in 'MF':
    info = input('Dados inválidos. Por favor, tente de novo: ')
print('Sexo {} registrado com sucesso!'.format(info))
