from time import sleep

def linha():
    print('-'*45)

def maior(*num):
    mai = 0
    linha()
    print('Analisando os valores...')
    linha()
    sleep(1)
    print(f'Os valores informados foram: ', end='')
    for n in num:
        print(n, end=' ')
        sleep(0.5)
    print()
    sleep(0.5)
    print(f'Foram informados {len(num)} elementos.')
    sleep(0.5)
    for n in num:
        if n > mai:
            mai = n
    print(f'O maior valor informado foi {mai}.')
    sleep(1)

maior(1, 4, 67, 45, 68, 65)
maior()

