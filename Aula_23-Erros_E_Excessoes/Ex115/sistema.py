from Ex115.lib.interface import *
from Ex115.lib.arquivo import *
from time import sleep

arq = 'cadastros.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Cadastrar Pessoas', 'Listar Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        cabecalho('Novo Cadastro')
        nome = input('Nome: ')
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 2:
        lerArquivo(arq)
    elif resposta == 3:
        print('Saindo do Sistema', end='')
        for ponto in range(0,3):
            print('.', end='')
            sleep(0.5)
        break
    else:
        print('\033[31mERRO! Digite uma opção válida.\033[m')
    sleep(2)