num = list()
maior = menor = 0
c = 1

for x in range(0,5):
    num.append(int(input(f'Digite um valor para a posição {x}: ')))
print('=-'*30)
print('Você digitou os valores', num)
for n in num:
    if c == 1:
        maior = menor = n
    else:
        if n >= maior:
            maior = n
        else:
            menor = n
    c += 1
        
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(num): #enumera cada valor da lista
    if v == maior:
        print(f'{i}...', end='')
print()
        
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(num): #enumera cada valor da lista
    if v == menor:
        print(f'{i}...', end='')
