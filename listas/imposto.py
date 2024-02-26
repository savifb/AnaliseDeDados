produtos = ['computador', 'livro', 'celular', 'tv', 'ar condicionado','alexa', 'maquina de cafe', 'kindle']
imposto = 1.1
produtos_ecommerce = [
    [1000, 5000], 
    [1500.50, 15000], 
    [150.99, 1000], 
    [1328.09, 5038.90],
    [100, 500],
    [50, 250],
    [329, 9503],
    [90, 8000],
]
if 'livro' in produtos:
    print('livro encontrado!')
    i_livro = produtos.index('livro')
    total_antigo = produtos_ecommerce[i_livro][0]*produtos_ecommerce[i_livro][1]
    produtos_ecommerce[i_livro][1] = produtos_ecommerce[i_livro][1] * imposto
    novo_total = produtos_ecommerce[i_livro][0]*produtos_ecommerce[i_livro][1]
    print('O valor antigo foi de R$ {:,} \n'.format(total_antigo))
    print('O valor novo com impostos foi de: R$ {:,} \n'.format(novo_total))
    print('O valor de imposto foi de R$ {:,}:'.format(novo_total - total_antigo))
    print(produtos_ecommerce)
else:
    print('livro não encontrado!')
    print(produtos_ecommerce)

