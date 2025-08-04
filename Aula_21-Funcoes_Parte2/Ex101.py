from datetime import date


def voto(ano):

    idade = date.today().year - ano

    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


ano_nasc = int(input('Em que ano você nasceu? '))
print(voto(ano_nasc))
