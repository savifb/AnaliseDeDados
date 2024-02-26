
estoque = [
    [213,31321,54,7676,87,445,8654,454,353,765],
    [678,987,654,321,345,678,987,654,321,345],
    [9986,765,432,123,456,789,987,654,321,345],
    [9876,543,210,987,654,321,345,678,987,654],
    [8765,432,109,876,543,210,987,654,321,345],
]
fabricas = ['SAVIO SA', 'LUIZA&SAVIO', 'SAVIO HSJ', 'SAVIOSAS', 'SAERO']
nivel_minimo_estoque = 135
fabricaEstoqueMinimo = []

for i, lista in enumerate(estoque):
    for qtd in lista:
        if qtd < nivel_minimo_estoque:
            print(qtd)
            if  fabricas[i] not in fabricaEstoqueMinimo:
                fabricaEstoqueMinimo.append(fabricas[i])
            
print(fabricaEstoqueMinimo)
