vendedores_dic = {'Maria': 1200, 'José': 300, 'Antônio': 800, 'João': 1500, 'Francisco': 1900, 'Ana': 2750, 'Luiz': 400, 'Paulo': 20, 'Carlos': 23, 'Manoel': 70, 'Pedro': 90, 'Francisca': 80, 'Marcos': 1100, 'Raimundo': 999, 'Sebastião': 900, 'Antônia': 880, 'Marcelo': 870, 'Jorge': 50, 'Márcia': 1111, 'Geraldo': 120, 'Adriana': 300, 'Sandra': 450, 'Luis': 800}
meta = 1000
bateram_meta = {}
bonus = []
for vendedor, valor_vendas in vendedores_dic.items():
    if valor_vendas >= meta:
        bateram_meta[vendedor] =round(valor_vendas*1.1)
        bonusis = valor_vendas*0.1
        bonus.append(bonusis) 
        print(f"Vendedor {vendedor} bateu a meta e recebeu bônus de {bonusis:.2f}")
    else:
        bonusis = 0
        bonus.append(bonusis)
print(bonus)
print(len(bateram_meta))

bateram_meta_2 = {(vendedor2, valor_vendas2) for vendedor2, valor_vendas2 in vendedores_dic.items() if valor_vendas2 >= meta}

print(len(bateram_meta_2))

bonus2 = [vendedores_dic[item]*0.1 if vendedores_dic[item] > meta else 0 for item in vendedores_dic]

print(bonus2)