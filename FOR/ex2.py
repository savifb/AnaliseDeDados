meta = 6000

vendedores = [
    ['julia', 15000],
    ['maria', 20000],
    ['pedro', 5000],
    ['joao', 10000],
    ['jose', 30000],
    ['jorge', 15000]
]
bateraMeta = []
i = 0
melhorVendedor = ''
maiorVenda = 0
for item in vendedores:
    if item[1]>=meta:
        print(f'Vendedor {item[0]} Vendeu {item[1]} e Bateu a meta!')
        bateraMeta.append(item)
        i=i+1
    else:
        print(f'Vendedor {item[0]} não bateu meta')
    if item[1]>maiorVenda:
        maiorVenda = item[1]
        melhorVendedor = item[0]
porCentagem = i/len(vendedores)
print(i)
print(len(vendedores))
print(f'{porCentagem*100}% dos vendedores bateram a meta')
print(bateraMeta)
print(f'O melhor vendedor foi {melhorVendedor} com {maiorVenda} vendas')

