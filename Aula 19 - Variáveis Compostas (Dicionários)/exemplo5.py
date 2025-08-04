estado = {}
brasil = []

for cont in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    #Realizar a cópia
    brasil.append(estado.copy())

for e in brasil:
    for k, v in e.items():
        print(f'{k} = {v}')
