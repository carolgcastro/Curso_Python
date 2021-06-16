word = ('aprender','programar',
        'linguagem','python',
        'curso','gratis', 'estudar',
        'praticar','trabalhar',
        'mercado','programador',
        'futuro')
for p in word:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for l in p:
        if l in 'aeiou':
            print(f'{l}', end=' ')
