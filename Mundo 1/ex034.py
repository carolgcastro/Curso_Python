sal = float(input('Qual é o salário do funcionário? R$ '))

if sal > 1250:
    total = (sal * 0.10) + sal
else:
    total = (sal * 0.15) + sal
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(sal, total))
