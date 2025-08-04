#Parâmetros Opcionais

# O "=0" do lado dos parâmetros significa que,
# caso algum deles não receba valor, sera igual á 0.
def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 5)
somar(8, 4)
somar(a=1, c=3)

