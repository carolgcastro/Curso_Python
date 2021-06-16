def fatorial(n, show=False):
    c = 1
    for x in range(n,0,-1):
        if show:
            print(x, end=' ')
            if x > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
        c *= x
    return c

print(fatorial(5, True))
print(fatorial(5)
