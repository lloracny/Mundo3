#Lista de preços com tupla

listagem = ('Pão', 3, 'Leite', 5, 'Carne', 20, 'Feijão', 15)

print('-'*40)
print('LISTAGEM DE PREÇOS'.center(40))
print('-'*40)
print()
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<32}', end='')
    else:
        print(f'R${listagem[pos]:>6.2f}')

print()
print('-'*40)