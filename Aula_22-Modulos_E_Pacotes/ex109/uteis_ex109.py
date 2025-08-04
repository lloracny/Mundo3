def metade(n=0, formato=False):
    res = n / 2
    return res if not formato else moeda(res)

def dobro(n=0, formato=False):
    res = n * 2
    return res if not formato else moeda(res)

def aumentar(n=0, p=0, formato=False):
    porcentagem = n + (n * (p / 100))
    return porcentagem if formato is False else moeda(porcentagem)

def diminuir(n=0, p=0, formato=False):
    porcentagem = n - (n * (p / 100))
    return porcentagem if formato is False else moeda(porcentagem)


def moeda(n =0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')