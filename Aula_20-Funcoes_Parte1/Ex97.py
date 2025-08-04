def escreva(txt):
    tamanho = len(txt) + 4
    print(f'-' * tamanho)
    print(f'{txt}'.center(tamanho))
    print(f'-' * tamanho)

texto = str(input('Digite algo: '))
escreva(texto)
