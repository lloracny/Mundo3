#Dividindo valores em varias Listas

numeros = []
pares = []
impares = []


while True:
    num = int(input('Digite um numero: '))
    numeros.append(num)

    resp = input('Deseja continuar? [S/N] ').strip().upper()[0]

    while resp != 'S' and resp != 'N':
        resp = input('Deseja continuar? [S/N] ').strip().upper()[0]

    if resp == 'N':
        break

for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    elif num % 2 == 1:
        impares.append(num)

print('-' * 50)
print(f'Os números inseridos na lista foram: {numeros}')
print()
print(f'Os números pares da lista foram: {pares}')
print(f'Os números impares da lista foram: {impares}')