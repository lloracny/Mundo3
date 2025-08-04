def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s).')


nome = str(input('Digite o nome do jogador: '))
gols = str(input('Digite a quantidade de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if nome.strip() == '':
    ficha(gols=gols)
else:
    ficha(nome, gols)