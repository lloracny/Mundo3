from ex109 import uteis_ex109
from uteis_ex109 import moeda

num = float(input('Digite um número: '))
print(f'A metade de {moeda(num)} é {uteis_ex109.metade(num, True)}')
print(f'O dobro de {moeda(num)} é {uteis_ex109.dobro(num, True)}')
print(f'Aumentando 10%, temos {uteis_ex109.aumentar(num, 10, True)}')
print(f'Reduzindo 10%, temos {uteis_ex109.diminuir(num, 10, True)}')