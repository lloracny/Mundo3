#Listas com Pares e Ímpares

lista = [[],[]]

for v in range(1,8):
    valor = int(input(f'Informe o {v}° valor: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)

lista[0].sort()
lista[1].sort()

print(f'Os valores pares informados foram: {lista[0]}')
print(f'Os valores impares informados foram: {lista[1]}')