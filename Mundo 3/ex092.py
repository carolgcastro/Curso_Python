from datetime import datetime
dici = dict()
dici['nome'] = input('Nome: ')
nasc = int(input('Ano de Nascimento: '))
dici['idade'] = datetime.now().year - nasc
dici['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dici['ctps'] == 0:
    print('-='*20)
    print(f'''- nome tem o valor {dici['nome']}
- idade tem o valor {dici['idade']}
- ctps tem o valor {dici['ctps']} ''')
else:
    dici['ano'] = int(input('Ano de Contratação: '))
    dici['salario'] = float(input('Salário: R$'))
    dici['apos'] = dici['idade']+(dici['ano'] + 35) - datetime.now().year
    print('-='*20)
    print(f'''- nome tem o valor {dici['nome']}
- idade tem o valor {dici['idade']}
- ctps tem o valor {dici['ctps']}
- salário tem o valor R${dici['salario']}
- aposentadoria tem valor {dici['apos']}''')
