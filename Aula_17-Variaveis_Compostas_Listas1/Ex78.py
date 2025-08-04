#Maior e Menor valores em Lista

valores = []
maior = menor = 0

for pos in range(0,5):
    valores.append(int(input(f'Informe o {pos+1}° valor: ')))

    if pos == 0:
        maior = valores[pos]
        menor = valores[pos]
    else:
        if maior < valores[pos]:
            maior = valores[pos]
        elif menor > valores[pos]:
            menor = valores[pos]

print('-='*30)
print(f'Os valores informados foram: {valores}')

print(f'O maior valor informado foi {maior} nas posições ', end='')
for indice, valor in enumerate(valores):
    if valor == maior:
        print(f'{indice+1}', end=', ')
print('FIM')

print(f'O menor valor informado foi {menor} nas posições ', end='')
for indice, valor in enumerate(valores):
    if valor == menor:
        print(f'{indice+1}', end=', ')
print('FIM')



