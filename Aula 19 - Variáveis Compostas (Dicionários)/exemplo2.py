filme = {
    'titulo': 'Star Wars',
    'ano': 1977,
    'diretor': 'George Lucas',
}

#Retorna os valores do dicionário
print(filme.values())

#Retorna as chaves
print(filme.keys())

#Retorna os valores e as chaves
print(filme.items())

#Utilizando for para visualizar as informações do dicionário
for k, v in filme.items():
    print(f'{k}: {v}')