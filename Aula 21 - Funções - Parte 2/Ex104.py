def leiaInt(n):
    while True:
        try:
            n = int(input(n))
            return n
        except (ValueError, TypeError):
            print(f'\033[31mERRO! Digite um número inteiro valido!\033[m')


n = leiaInt('Digite um numero inteiro: ')
print(f'Você digitou o numero {n}')