#Mais sobre Matriz em Python

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

soma = 0
soma_col = 0
maior = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        if matriz[linha][coluna] % 2 == 0:
            soma += matriz[linha][coluna]

print('-'*30)

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()

print('-'*30)

print(f'A soma dos valores pares é de: {soma}.')

for linha in range(0, 3):
    soma_col += matriz[linha][2]
print(f'A soma dos valores da terceira coluna é de: {soma_col}.')

for coluna in range(0, 3):
    if coluna == 0:
        maior = matriz[1][coluna]
    else:
        if maior < matriz[1][coluna]:
            maior = matriz[1][coluna]
print(f'O maior valor da segunda linha é de: {maior}.')

print('-'*30)
