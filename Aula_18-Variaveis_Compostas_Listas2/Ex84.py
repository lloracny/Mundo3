#Lista Composta e Análise de Dados

dados = []
lista = []
cadastro = 0
leve = pesado = 0

while True:
    dados.append(input('Digite o nome da pessoa: '))
    dados.append(float(input('Digite o peso da pessoa (Em KG): ')))

    if cadastro == 0:
        leve = pesado = dados[1]
    else:
        if dados[1]> pesado:
            pesado = dados[1]
        elif dados[1] < leve:
            leve = dados[1]

    lista.append(dados[:])
    dados.clear()
    cadastro += 1


    resp = input('Deseja continuar? [S/N] ').strip().upper()[0]

    while resp not in 'SN':
        resp = input('Deseja continuar? [S/N] ').strip().upper()[0]

    if resp in 'N':
        break

print('-'*30)
print(f'Foram cadastradas {cadastro} pessoa(s).')
print('-'*30)

print(f'O maior peso foi de {pesado:.2f}KG. Peso de: ', end='')
for pessoa in lista:
    if pessoa[1] == pesado:
        print(f'[{pessoa[0]}]', end=', ')
print('FIM')

print(f'O menor peso foi de {leve:.2f}KG. Peso de: ', end='')
for pessoa in lista:
    if pessoa[1] == leve:
        print(f'[{pessoa[0]}]', end=', ')
print('FIM')
