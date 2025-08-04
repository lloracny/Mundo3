try: #Operação
    n1 = int(input('Numerador: '))
    n2 = int(input('Denominador: '))
    r = n1 / n2

#except Exception as erro: #Caso falhe
#    print(f'Problema encontrado foi {erro.__class__}')

except (ValueError, TypeError):
    print(f'Tivemos problemas com os tipos de dados.')
except ZeroDivisionError:
    print(f'Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print(f'O usuário não informou os dados.')

else: #Caso de certo

    print(f'O resultado foi {r:.1f}')

finally: #Sempre acontece, independentemente do
        #sucesso do código.
    print('Volte sempre!')