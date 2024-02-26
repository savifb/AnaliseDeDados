def metas_atingidas(meta, vendas):
    vendedor_metados = []
    for vendedor in vendas:
         valor = vendas[vendedor]
         if valor >= meta:
            vendedor_metados.append(vendedor)
    percentual = len(vendedor_metados)/len(vendas)
    return (vendedor_metados, percentual )


meta = 10000
vendas = {
    'João': 15000,
    'Julia': 27000,
    'Marcus': 9900,
    'Maria': 3750,
    'Ana': 10300,
    'Alon': 7870,
}

print(metas_atingidas(meta, vendas))