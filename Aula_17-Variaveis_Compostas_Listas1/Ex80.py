#lista ordenada sem sort()

numeros = list()

for posicao in range(0, 5):
    num = int(input('Digite um valor: '))

    if posicao == 0 or num > numeros[-1]:
        numeros.append(num)
    else:
        pos = 0
        while pos < len(numeros):
            if num <= numeros[pos]:
                numeros.insert(pos, num)
                break
            pos += 1

print('-' * 30)
print(f'Os valores digitados em ordem foram {numeros}')
