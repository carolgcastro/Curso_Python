lista = []
nome = input('Digite um nome: ')
peso = float(input('Peso: '))
c = 0
while True:
    c +=1 
    pessoa = [nome, peso]
    lista.append(pessoa)
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        else:
            menor = peso
    n = input('Deseja continuar? [S/N] ')
    if 'n' == n:
        break
    nome = input('Digite um nome: ')
    peso = float(input('Peso: '))
print(f'''Ao todo, você cadastrou {len(lista)} pessoas.
O maior peso foi {maior:.1f}Kg. Peso de 
O menor peso foi {menor:.1f}Kg. Peso de''')
'''falta de quem é o peso'''
