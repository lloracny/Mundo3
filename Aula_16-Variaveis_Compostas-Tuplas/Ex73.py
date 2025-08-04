#Tuplas com Times de Futebol
from time import sleep

times = ('Flamengo', 'Cruzeiro', 'Bragantino', 'Palmeiras', 'Bahia', 'Fluminense', 'Atlético-MG', 'Botafogo', 'Mirassol', 'Corinthians', 'Grêmio', 'Ceará SC', 'Vasco da Gama', 'São Paulo', 'Santos', 'EC Vitória', 'Internacional', 'Fortaleza', 'Juventude', 'Sport Recife')
posicao = times.index('Palmeiras')

print(f'Os 5 primeiros colocados são: {times[:5]}.')
sleep(0.5)
print(f'Os 4 últimos colocados são: {times[-4:]}.')
sleep(0.5)
print(f'Times em ordem alfabética: {sorted(times)}.')
sleep(0.5)
print(f'O time do Palmeiras está na {posicao}° posição.')

