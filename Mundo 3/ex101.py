from datetime import datetime
def voto(ano):
    idade = datetime.now().year - ano
    if idade < 16:
        return f'{idade} anos: NÃO VOTA'  
    elif 16 <= idade < 18 or idade > 65:
        return f'{idade} anos: VOTO OPCIONAL'
    else:
        return f'{idade} anos: VOTO OBRIGATÓRIO'

res = voto(int(input('Em que ano você nasceu? ')))
print(res)
