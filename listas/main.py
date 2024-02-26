produtos = ['geladeira', 'macarrão', 'fogão', 'palhaço', 'cama', 'borracha']
preco = [1500, 10, 1800, 2300, 1200, 1.50]

produtos.append('joséfino')
preco.append(54)



print(produtos)


tamanho_produtos = len(produtos)
print(tamanho_produtos)
tamanho_preco = len(preco)
print(tamanho_preco)

print(produtos)
print(preco)

maior_valor = max(preco)
menor_valor = min(preco)
print(maior_valor)

index_maior_valor = preco.index(maior_valor)
produto_maior_valor = produtos[index_maior_valor]
print(produto_maior_valor)

index_menor_valor = preco.index(menor_valor)
produto_menor_valor = produtos[index_menor_valor]
print(produto_menor_valor)

produtos.sort(reverse=True)
print(produtos)