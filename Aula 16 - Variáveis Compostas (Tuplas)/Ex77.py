palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudante', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')

vogais = ('a', 'e', 'i', 'o', 'u')

for palavra in palavras:
        print(f'Na palavra {palavra.upper()} temos as vogais: ', end='')
        for vogal in vogais:
            if vogal in palavra:
                print(f'{vogal}', end=' ')
        print()
