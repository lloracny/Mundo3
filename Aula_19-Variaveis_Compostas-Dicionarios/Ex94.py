from time import sleep

pessoa = {}
cadastros = []
soma_idade = 0

cont = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo: [M/F]: ')).strip().upper()[0]
    while pessoa['sexo'] not in 'MF':
        pessoa['sexo'] = str(input('Sexo: [M/F]: ')).strip().upper()[0]
    pessoa['idade'] = int(input('Idade: '))

    cont += 1
    soma_idade += pessoa['idade']
    cadastros.append(pessoa.copy())

    resp = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    while resp not in 'SN':
        resp = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    if resp == 'N':
        break

media_idade = float(soma_idade / cont)


print(f'Foram cadastradas {cont} pessoas.')

sleep(0.5)

print(f'A média de idade é de {media_idade:.2f} anos.')

sleep(0.5)

print(f'As mulheres cadastradas foram: ', end='')
for mulher in cadastros:
    if mulher['sexo'] == 'F':
        print(f'{mulher["nome"]}', end= ', ')
print('FIM')

sleep(0.5)

print(f'As pessoas com idade acima da média cadastradas foram: ', end='')
for acima_media in cadastros:
    if acima_media['idade'] > media_idade:
        print(f'\n   Nome: {acima_media["nome"]}; Sexo: {acima_media["sexo"]}; Idade: {acima_media["idade"]}')
