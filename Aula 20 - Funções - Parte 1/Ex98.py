from time import sleep

def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo = abs(passo) #Abs transforma um número negativo em sua versão positiva.
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(1)
    if inicio < fim:
        for c in range(inicio, fim + 1, passo):
            print(c, end=' ')
            sleep(0.5)
        print('FIM')
    elif inicio > fim:
        for c in range(inicio, fim - 1, -passo):
            print(c, end=' ')
            sleep(0.5)
        print('FIM')

print('Agora é sua vez!')
contador(1, 10, 1)
contador(10, 0, 2)
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
