nome = input(' Digite seu nome completo: ').strip()

div_n = nome.split()

print(' Muito prazer em te conhecer\n Seu primeiro nome é {}\n Seu último nome é {}'.format(div_n[0], div_n[-1]))
