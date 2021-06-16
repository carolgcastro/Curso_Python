print('='*30)
print('      BANCO CEV')
print('='*30)
valor = int(input('Qual valor você quer sacar? R$'))
total = valor
ced = 50
total_c = 0
while True:
    if total >= ced:
        total -= ced
        total_c += 1
    else:
        if total_c > 0:
            print(f'Total de {total_c} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        total_c = 0
        if total == 0:
            break
print('='*30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
