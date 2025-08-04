#Número por Extenso
from time import sleep

num_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

print('-' * 40)
print('NÚMERO POR EXTENSO'.center(40))
print('-' * 40)

sleep(0.5)

num = int(input('Informe um número no intervalo de 0 á 20: '))

while True:
    if num > 20:
        num = int(input('O número informado é maior que 20.'
                        '\nInforme um número no intervalo de 0 á 20: '))
    if num < 0:
        num = int(input('O número informado é menor que 0.'
                  '\nInforme um número no intervalo de 0 á 20: '))
    else:
        break

num_extenso = num_extenso[num]

print(f'Você digitou o número {num_extenso}.')



