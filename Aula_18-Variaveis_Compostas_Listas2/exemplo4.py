galera = list()
dado = list()
maior = menor = 0

for cont in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for pessoa in galera:
    if pessoa[1] >= 20:
        print(f'{pessoa[0]} é maior de idade.')
        maior += 1
    else:
        print(f'{pessoa[0]} é menor de idade.')
        menor += 1

print(f'Total de maior de idade: {maior}')
print(f'Total de menor de idade: {menor}')
