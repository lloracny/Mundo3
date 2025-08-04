import uteis_ex108
from uteis_ex108 import moeda

num = float(input('Digite um número: '))
print(f'A metade de {moeda(num)} é {moeda(uteis_ex108.metade(num))}')
print(f'O dobro de {moeda(num)} é {moeda(uteis_ex108.dobro(num))}')
print(f'Aumentando 10%, temos {moeda(uteis_ex108.aumentar(num, 10))}')
print(f'Reduzindo 10%, temos {moeda(uteis_ex108.diminuir(num, 10))}')