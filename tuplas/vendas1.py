vendas_produtos = [
    ('Iphone', 558147, 951642),
    ('Galaxy', 573819, 288322),
    ('Ipad', 48382, 83291),
    ('tv', 32831, 54831),
]

for produto, vendas2019, vendas2020 in vendas_produtos:
    crescimento = ((vendas2020/vendas2019)-1)
    if vendas2020 >= vendas2019:
        print(f'Vendas 2020 que foram maiores que 2019: {vendas2020}\n')
        print(f'O crescimento do produto {produto} foi de: {crescimento:.1%}\n ')

