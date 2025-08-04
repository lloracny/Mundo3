def ajuda(resp):
    if resp == 'fim':
        print('Obrigado por usar o sistema!')
    else:
        print('-'*40)
        print(f'Acessando o manual do comando "{resp}"')
        print('-' * 40)
        help(resp)


while True:
    print('*'*30)
    print('SISTEMA DE AJUDA'.center(30))
    print('*'*30)
    perg = input('Função ou Biblioteca: ').lower()
    ajuda(perg)
    if perg == 'fim':
        break