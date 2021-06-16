from datetime import date
ano = int(input('Ano de nascimento: '))
atual = date.today().year #ano atual
idade = atual - ano

print('Quem nasceu em {} tem {} anos em {}'.format(ano, idade, atual))

if idade < 18:
    print('Ainda faltam {} anos para o alistamento.'.format(18 - idade))
    print('Seu alistamento será em {}'.format(atual + (18 - idade)))
elif idade > 18:
    print('Você já deveria ter se alistado há {} anos.'.format(idade - 18))
    print('Seu alistamento foi em {}.'.format(atual - (idade - 18)))
else:
    print('Você tem que se alistar IMEDIATAMENTE!')
    
