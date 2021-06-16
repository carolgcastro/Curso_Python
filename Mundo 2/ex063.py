print('-'*25)
print('Sequência de Fibonacci')
print('-'*25)
n = int(input('Quantos termos você quer mostrar? '))
c = 3
num = 0
num_2 = 1

print('{} - {}'.format(num, num_2), end=' - ')
while c <= n:
    num_3 = num + num_2
    num = num_2
    num_2 = num_3
    #num += num_2 outra opção
    #c += 1
    #num_2 += num
    c += 1
    print('{}'.format(num_3), end=' - ')
    #print('{}'.format(num_2), end=' - ')
print('FIM')
