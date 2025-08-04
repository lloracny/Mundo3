#Valores únicos em uma Lista

numeros = list()

while True:
    num = int(input('Digite um numero: '))
    if num not in numeros:
        numeros.append(num)
    else:
        print('Este número já foi adicionado! Informe outro.')

    resp = input('Deseja continuar? [S/N] ').strip().upper()[0]

    while resp != 'S' and resp != 'N':
        resp = input('Deseja continuar? [S/N] ').strip().upper()[0]

    if resp == 'N':
        break

numeros.sort()

print(f'Os números adicionados á lista foram: {numeros}')




