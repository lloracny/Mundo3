a = [2, 3, 4, 7]
# = a #-> Dessa forma, esta fazendo uma LIGAÇÃO entre as listas
b = a[:] #-> Dessa forma, cria apenas uma cópia
b[2] = 8
print(f'Lista a: {a}')
print(f'Lista b: {b}')