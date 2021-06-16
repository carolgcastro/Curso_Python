cont = 0
dici = {}
dici['nome'] = input('Nome do Jogador: ')
dici['part'] = int(input(f'Quantas partidas {dici["nome"] jogou? }'))
for i in range(dici['part']):
    dici['gols'] = int(input(f'Quantos gols na partida {i+1}'))
    cont += dici['gols']
dici['total'] = cont

print('-='*20)
print(dici)
print('-='*20)
print(f'''O campo nome tem valor {dici["nome"]}
O campo gols tem o valor {dici["gols"]}
O campo total tem o valor {dici["total"]}''')
print('-='*20)
print(f'O jogador {dici["nome"]} jogou {dici["part"]}')
for i in range(dici['part']):
    print(f'=> Na partida {i+1}, fez {dici["gols"][i]}.')
print(f'Foi um total de {dici["total"]} gols.')
