#Mostra a posição onde esta o elemento 

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

for pos, comer in enumerate(lanche):
    print(f'Eu vou comer {comer} na pos {pos}')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posicao {cont}')