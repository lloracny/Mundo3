from datetime import date
from time import sleep

dados = {}
aposentar = 0

dados['nome'] = input('Informe seu nome: ')

nasc = int(input('Informe o ano de nascimento: '))
idade = date.today().year - nasc
dados['idade'] = idade

dados['ctps'] = int(input('Informe sua CTPS (0 caso não tenha): '))


if dados['ctps'] != 0:
    dados['ano_contratacao'] = int(input('Informe o ano de contratação: '))
    dados['salario'] = float(input('Informe o salário: R$'))

    anos_trabalhando = date.today().year - dados['ano_contratacao']
    anos_faltando = 35 - anos_trabalhando
    aposentar = anos_faltando + idade
    dados['idade_aposentar'] = aposentar


sleep(1)
print('-'*40)
print('INFORMAÇÕES CADASTRADAS'.center(40))
print('-'*40)
sleep(1)

print(f'Nome: {dados["nome"]}')
sleep(0.5)
print(f'Idade: {dados["idade"]}')
sleep(0.5)
print(f'CTPS: {dados["ctps"]}')
sleep(0.5)

if dados['ctps'] != 0:
    print(f'Ano de contratação: {dados["ano_contratacao"]}')
    sleep(0.5)
    print(f'Salário: R${dados["salario"]:.2f}')
    sleep(0.5)
    print(f'Você poderá se aposentar com {aposentar} anos.')