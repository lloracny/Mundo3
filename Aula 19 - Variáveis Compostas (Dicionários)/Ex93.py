from time import sleep

dados = {}
quant = []
soma = 0

dados['nome'] = input('Nome do jogador: ')
dados['partidas'] = int(input('Partidas jogadas: '))
dados['gols'] = []

for partida in range(1, dados['partidas']+1):
    quant.append(int(input(f'Quantos gols foram feitos na {partida}° partida? ')))
    dados['gols'] = quant[:]
    soma += quant[-1]
    dados['total'] = soma

sleep(1)
print('-'*70)
print(dados)
print('-'*70)
sleep(1)

print(f'Nome do jogador: {dados["nome"]}')
sleep(0.5)
print(f'Partidas jogadas: {dados["partidas"]}')
sleep(0.5)
print(f'Gols feitos: {dados["gols"]}')
sleep(0.5)
print(f'Total de gols: {dados["total"]}')
print('-'*40)
sleep(1)

print(f'O jogador {dados["nome"]} jogou {dados["partidas"]} partidas.')
sleep(1)

for p, g in enumerate(dados["gols"]):
    print(f'- {p+1}° Partida: {g} gols.')
    sleep(0.5)

print(f'Foi um total de {dados["total"]} gols.')


