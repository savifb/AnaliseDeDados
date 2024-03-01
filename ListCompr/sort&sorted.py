produtos = ['apple tv', 'mac', 'IPhone x', 'IPhone 11', 'IPad', 'apple watch', 'mac book', 'airpods']
produtos.sort(key=str.casefold)
print(produtos)

vendas_produtos = {'vinho': 100, 'cafeiteira': 150, 'microondas': 300, 'iphone': 5500}

def ordenaSegundo(texto):
    return texto[1]

list_vendasProdutos = list(vendas_produtos.items())
list_vendasProdutos.sort(key=ordenaSegundo, reverse=True)

print(list_vendasProdutos)