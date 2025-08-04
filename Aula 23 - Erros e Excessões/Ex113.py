def leiaint(numero):
    while True:
        try:
            numero = int(input(numero))
            return numero
        except KeyboardInterrupt:
            print(f'\033[31mUsuário preferiu não digitar esse número!\033[m')
            return 0
        except (ValueError, TypeError, ZeroDivisionError):
            print(f'\033[31mERRO! Digite um número inteiro válido!\033[m')
            continue

def leiafloat(numero):
    while True:
        try:
            numero = float(input(numero))
            return numero

        except KeyboardInterrupt:
            print(f'\033[31mUsuário preferiu não digitar esse número!\033[m')
            return 0
        except (ValueError, TypeError, ZeroDivisionError):
            print(f'\033[31mERRO! Digite um número real válido!\033[m')
            continue


n = leiaint('Digite um numero inteiro: ')
n2 = leiafloat('Digite um numero real: ')

print(f'Número inteiro: {n}')
print(f'Número real: {n2}')
