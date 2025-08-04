def ficha(nome, gol):
    if nome.strip() == '':
        nome = "<desconhecido>"
    if gol.isnumeric():
        gol = int(gol)
    else:
        gol = 0
    print(f'O jogador {nome} fez {gol} gol(s).')


nome = str(input('Digite o nome do jogador: '))
gols = str(input('Digite a quantidade de gols: '))
ficha(nome, gols)