#DocStrings
def contador(i,f,p):
    #Adiciona uma descrição com 3 aspas duplas (")
    #e adiciona a descrição da função.
    """-> Faz uma contagem e mostra na tela.
    i: inicio da contagem
    f: fim da contagem
    p: passo da contagem
    return: sem retorno"""
    for c in range(i,f+1,p):
        print(f'{c}', end=' ')
    print()

help(contador) # -> Visualiza a descrição da função.
