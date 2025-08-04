def fatorial(numero, show=False):
    """
    -> Calcula o fatorial de um numero.
    :param numero: numero a ser calculado.
    :param show: (opcional) mostra o calculo do fatorial.
    """
    f = 1
    for c in range(numero, 0, -1):
        f *= c

    if show:
        cont = numero
        print('-'*30)
        while cont > 1:
            print(cont, end=' x ')
            cont -= 1
        print('1', end=' ')
        print(f'= {f}', end=' ')
    else:
        print(f'O fatorial de {numero} é {f}')


num = int(input('Digite um número: '))
opcao = (input('Deseja ver o cálculo? (S/N): ')).strip().upper()[0]

while opcao != 'S' and opcao != 'N':
    opcao = (input('Deseja ver o cálculo? (S/N): ')).strip().upper()[0]
 
if opcao == 'S':
    show = True
    fatorial(num, show)
elif opcao == 'N':
    show = False
    fatorial(num, show)


