from time import sleep
def maior(* num):
    print('-='*30)
    print(f'Analisando os valores passados...')
    c = maior = 0
    for x in num:
        if c == 0:
            maior = x
            c += 1
        else:
            if x > maior:
                maior = x
        print(x, end=' ', flush=True)
        sleep(.5)
    print(f'''Foram informados {len(num)} valores ao todo.
O maior valor informado foi {maior}''')

maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()
