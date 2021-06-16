from time import sleep
def cont(i,f,p):
    if i < f:
        print('-='*20)
        for x in range(i,f+1,p):
            print(x, end=' ')
        print('FIM!')
        print('-='*20)
    else:
        cont = i
        while cont >= f:
            print(cont, end=' ')
            cont -= p
        print('FIM!')
        print('-='*20)

cont(0,10,1)
cont(10,0,2)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
cont(i,f,p)
