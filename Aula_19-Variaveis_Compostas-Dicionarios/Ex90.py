dados = dict()

nome = input('Qual é o seu nome? ')
media = float(input(f'Qual é a média de {nome}? '))

situacao = ''

if media >= 7:
    situacao = 'Aprovado'
elif 5 <= media < 7:
    situacao = 'Recuperação'
else:
    situacao = 'Reprovado'

dados['nome'] = nome
dados['media'] = media
dados['situacao'] = situacao

for k, v in dados.items():
    print(f' - {k}: {v}')
