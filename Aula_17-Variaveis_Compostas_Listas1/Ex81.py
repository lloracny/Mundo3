#Extraindo dados de uma Lista

numeros = list()

while True:
    num = int(input('Digite um numero: '))
    numeros.append(num)

    resp = input('Deseja continuar? [S/N] ').strip().upper()[0]

    while resp != 'S' and resp != 'N':
        resp = input('Deseja continuar? [S/N] ').strip().upper()[0]

    if resp == 'N':
        break

numeros.sort(reverse=True)

print('-' * 40)
print(f'Você digitou {len(numeros)} elementos.')
print(f'Os elementos inseridos foram: {numeros}')
if 5 in numeros:
    print('O valor 5 está na lista.')

    #Adicional para visualizar as posições em que o 5 está.
    posicoes = []
    for c in range(0, len(numeros)):
        if numeros[c] == 5:
            posicoes.append(c+1)

    print(f'Ele aparece nas posições: {posicoes} ')
else:
    print('O valor 5 não foi digitado.')