def leiaint(msg):
    while True:
        try:
            numero = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mERRO! Digite um número inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\033[31mUsuário preferiu não digitar esse número!\033[m')
            return 0
        else:
            return numero

def linha(tamanho = 42):
    return '='*tamanho

def cabecalho(texto):
    print(linha())
    print(texto.center(42))
    print(linha())

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    cont = 1
    for item in lista:
        print(f'{cont} - {item}')
        cont += 1
    print(linha())
    opc = leiaint('Sua Opção: ')
    return opc