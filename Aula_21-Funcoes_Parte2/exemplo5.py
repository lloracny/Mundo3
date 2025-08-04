#Retornando Valores

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


#print(somar(3, 2, 5))
r1 = somar(3, 2, 5)
r2 = somar(1, 6, 2)
r3 = somar(2, 2, 1)
print(f'Meus cálculos deram {r1}, {r2} e {r3}')