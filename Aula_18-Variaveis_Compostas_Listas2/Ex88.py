#Palpites para Mega Sena

from random import randint
from time import sleep

lista = list()
jogos = list()

quant = int(input('Quantos jogos deseja realizar? '))
total = 1

while total <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1

sleep(0.5)
print()
print(f'SORTEANDO {quant} JOGOS...'.center(30, ' '))
print()
sleep(1)

for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(0.5)


