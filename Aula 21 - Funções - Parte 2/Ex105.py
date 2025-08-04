

def notas(* n, sit=False):
    dados = dict()
    dados['total'] = len(n)
    dados['maior'] = max(n)
    dados['menor'] = min(n)
    dados['media'] = sum(n) / len(n)
    if sit:
        if dados['media'] >= 7:
            dados['situacao'] = 'BOA'
        elif dados['media'] >= 5:
            dados['situacao'] = 'RAZOÁVEL'
        else:
            dados['situacao'] = 'RUIM'

    return dados


resp = notas(5.5, 3, 6, 2, sit=True)
print(resp)
