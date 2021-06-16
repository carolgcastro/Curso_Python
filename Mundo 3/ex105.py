def notas(* n, sit=False):
    dici = {}
    dici['total'] = len(n)
    dici['maior'] = max(n)
    dici['menor'] = min(n)
    dici['média'] = sum(n)/len(n)
    if sit:
        if dici['média'] >= 7:
            dici['situação'] = 'BOA'
        elif dici['média'] >= 5:
            dici['situação'] = 'RAZOÁVEL'
        else:
            dici['situação'] = 'RUIM'
    return dici

res = notas(5.5, 9.5, 10, 6.5, sit=True)
print(res)
