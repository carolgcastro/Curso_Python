dici = dict()
dici['nome'] = input('Nome: ')
dici['media'] = float(input(f'Média de {dici["nome"]}: '))
if dici['media'] > 7:
    dici['situ'] = 'Aprovado'
elif 5 < dici['media']  < 7:
    dici['situ'] = 'Recuperação'
else:
    dici['situ'] = 'Reprovado'

print('-='*20)
print(f'''- nome é igual a {dici["nome"]}
- média é igual a {dici["media"]}
- situação é igual a {dici["situ"]}''')
