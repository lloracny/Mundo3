from random import randint
from time import sleep
from operator import itemgetter

valores = dict()

for c in range(0, 4):
    valores[c] = randint(0, 10)
    sleep(1)
    print(f'O jogador {c+1} tirou {valores[c]}')

sleep(1)
print('-'*40)
print('RANKING DOS JOGADORES:'.center(40))
print('-'*40)
sleep(1)

ranking = sorted(valores.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: Jogador {v[0]+1} com {v[1]}.')
    sleep(1)


