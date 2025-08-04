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


def moeda(n =0):
    return f'{n:.2f}'.replace('.', ',')

def resumo(n=0,p1=0,p2=0):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'{"Preço analisado:":<20} {"R$"}{moeda(n)}')
    print(f'{"Dobro do Preço:":<20} {"R$"}{dobro(n, True)}')
    print(f'{"Metade do Preço:":<20} {"R$"}{metade(n, True)}')
    print(f'{p1}{"% de Aumento:":<18} {"R$"}{aumentar(n, p1, True)}')
    print(f'{p2}{"% de Redução:":<18} {"R$"}{diminuir(n, p2, True)}')
    print('-' * 30)