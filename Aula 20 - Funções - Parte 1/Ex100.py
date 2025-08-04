from random import randint
from time import sleep

numeros = list()

def sorteia(lista):
    for num in range(0, 5):
        lista.append(randint(1, 10))

    print('Sorteando', end='')
    for p in range(0, 3):
        print('.', end='')
        sleep(0.5)

    print('\nValores sorteados: ', end='')
    for num in lista:
        print(f'{num}', end=' ')
        sleep(0.5)


def somaPar(lista):
    soma = 0
    print('\nA soma dos valores pares (', end='')
    for num in lista:
        if num % 2 == 0:
            soma += num
            print(f'{num}', end=', ')
    print('FIM)', end='')
    print(f' é de {soma}')

sorteia(numeros)
somaPar(numeros)