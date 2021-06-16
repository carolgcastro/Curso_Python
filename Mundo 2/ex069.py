maior = 0
m = 0
f_menor = 0

while True:    
    print('-'*30)
    print('CADASTRE UMA PESSOA')
    print('-'*30)
    idade = int(input('Idade: '))
    if idade > 18:
        maior += 1
    sexo = input('Sexo [F/M]').upper()
    if sexo == 'M':
        m += 1
    elif sexo == 'F':
        if idade < 20:
            f_menor += 1
    print('-'*30)
    op = input('Quer continuar? [S/N]').upper()
    if op == 'N':
        break
print(f"""Total de pessoas com mais de 18 anos: {maior}
Ao todo temos {m} homens cadastrados
E temos {f_menor} mulheres com menos de 20 anos""")
