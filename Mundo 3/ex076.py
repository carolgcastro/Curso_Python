print('-'*40)
print(f"{'LISTAGEM DE PREÇOS':^40}")
#centralizado em 40 posiçoes
print('-'*40)

itens = ('Lápis', 1.75, 'Borracha', 2, 'Caderno',
         15.90, 'Estojo', 25, 'Transferidor', 4.2,
         'Compasso', 9.99, 'Mochila', 120.32,
         'Canetas', 22.3, 'Livro', 34.90)
for pos in range(0, len(itens)):
    if pos % 2 == 0:
        print(f'{itens[pos]:.<30}', end='')
        #mostrar alinhado a esquerda com . em 30 caracteres
    else:
        print(f'R${itens[pos]:>7.2f}')
        #alinhado a direita com 10 posições
print('-'*40)    
    
