def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

#Com Input
n = int(input('Digite um número: '))
print(f'O fatorial de {n} é {fatorial(n)}')

#Com mais de uma variável
f1 = fatorial(1)
f2 = fatorial(2)
f3 = fatorial(3)
print(f'Os resultados são: {f1}, {f2} e {f3}')