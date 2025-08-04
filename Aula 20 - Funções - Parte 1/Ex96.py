def area(larg, comp):
    a = larg * comp
    print(f'A área do terreno {larg}x{comp} é de: {a}m²')

def titulo(msg):
    print('-'*30)
    print(msg.center(30))
    print('-'*30)


titulo('Controle de Terrenos')

l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)