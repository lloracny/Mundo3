#Análise de Dados em uma Tupla

n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))
n3 = int(input('Digite o 3º valor: '))
n4 = int(input('Digite o 4º valor: '))

valores = (n1, n2, n3, n4)

print(f'Você digitou os valores {valores}.')

if 9 in valores:
    print(f'O valor 9 apareceu {valores.count(9)} vez(es).')
else:
    print('O valor 9 não apareceu.')

if 3 in valores:
    print(f'O valor 3 apareceu na {valores.index(3)+1}° posição.')
else:
    print('O valor 3 não apareceu.')

print(f'Os valores pares digitados foram: ', end='')
for pares in valores:
    if pares % 2 == 0:
        print(f'{pares}', end=', ')

print('FIM')