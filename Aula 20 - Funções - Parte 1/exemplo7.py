def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'A soma de {valores} é {s}')

soma(4, 5, 6)