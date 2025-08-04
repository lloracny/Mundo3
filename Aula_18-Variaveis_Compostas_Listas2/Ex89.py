#Boletim com Listas Compostas

lista = list()

while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])

    continuar = input('Deseja continuar? [S/N] ').strip().upper()[0]

    while continuar not in 'SsNn':
        continuar = input('Deseja continuar? [S/N] ').strip().upper()[0]

    if continuar in 'Nn':
        break


print('-'*30)
print('BOLETIM'.center(30, ' '))
print('-'*30)

print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')

print('-'*30)

for i, l in enumerate(lista):
    print(f'{i:<4}{l[0]:<10}{l[2]:>8.1f}')

while True:
    mostrar = int(input('Mostrar notas de qual aluno? (999 interrompe): '))

    if mostrar <= len(lista)-1:
        print(f'Notas de {lista[mostrar][0]} são {lista[mostrar][1]}')

    if mostrar == 999:
        break


