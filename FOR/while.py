x

produtos = []
print('Aperte enter sem digitar nada para sair do sistema')

while True:
    produto = input("Qual o produto: ")
    if not produto:
        break
    qtd = int(input("Quantidade: "))
    produtos.append([produto, qtd])
    produto = input("Qual o produto: ")
    qtd = int(input("Quantidade: "))

print('\n'.join(produtos))
