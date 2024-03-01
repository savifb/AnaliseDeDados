meta = 1600
vendas_produtos = [1500, 150, 2100, 1950]
produtos = ['vinho', 'cafeiteira', 'microondas', 'iphone']

for i in enumerate(produtos):
    print(i)
for i in produtos:
    print(i)
produtos_meta = []

for i,produto in enumerate(produtos):
    if vendas_produtos[i] >= meta:
        produtos_meta.append(produto)
print(produtos_meta)

list_vendas_maior = [produtos for i, produtos in enumerate(produtos) if vendas_produtos[i] >= meta]

print(list_vendas_maior)