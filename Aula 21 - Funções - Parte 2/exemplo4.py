#Escopo de Variáveis

#Escopo Local
def teste(b):
    global a #Transforma o A global no valor do A local
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

#Escopo global
a = 5
print(f'A fora vale {a}')
teste(a)
print(f'A fora vale {a}')