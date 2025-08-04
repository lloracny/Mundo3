jogador = {}
jogadores = []


while True:
    print('-'*50)
    jogador['nome'] = input('Nome do jogador: ')
    jogador['partidas'] = int(input('Partidas jogadas: '))

    jogador['gols'] = []
    jogador['total'] = 0

    for partida in range(1, jogador['partidas'] + 1):
        gols = int(input(f'Quantos gols foram feitos na {partida}° partida? '))
        jogador['gols'].append(gols)
        jogador['total'] += gols

    jogadores.append(jogador.copy())


    resp = input('Deseja continuar? [S/N] ').strip().upper()[0]

    while resp not in 'SN':
        resp = input('Deseja continuar? [S/N] ').strip().upper()[0]

    if resp == 'N':
        break

print('-='*25)
print(f'{"Cód.":<6}{"Nome":<10}{"Gols":<20}{"Total":<8}')
print('-'*30)

for i, jogador in enumerate(jogadores):
    print(f'{i:<6}{jogador["nome"]:<10}{str(jogador["gols"]):<20}{jogador["total"]:<8}')


while True:
    mostrar = int(input('Mostrar dados de qual jogador? (999 para interromper): '))

    if mostrar <= len(jogadores)-1:
        print(f'{"-="*30}')
        print(f'Levantamento do jogador: {jogadores[mostrar]["nome"].upper()}')
        print('-'*35)
        for i, gols in enumerate(jogadores[mostrar]["gols"]):
            print(f'- No jogo {i+1}, foram {gols} gols.')
    elif mostrar == 999:
        break
    elif mostrar > len(jogadores)-1:
        print('-'*50)
        print('Nenhum jogador foi encontrado. Tente novamente.')
        print('-' * 50)

print('ENCERRANDO...')
