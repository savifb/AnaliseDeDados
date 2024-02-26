precos = {"celular": 1500, "camera": 1000, "fone de ouvido": 800, "monitor": 2000}

""" 
while True:
    print("--- Digite sair Para sair do programa ----")
    consulta_usuario = input('Digite o nome do produto que deseja localizar: \n')
    if consulta_usuario in precos:
        print(f'O produto custa: {precos[consulta_usuario]}')
    elif consulta_usuario == 'sair':
        break
    decisao = input('O senhor(a) deseja cadastrar um produto?')
    if decisao == 'sim':
        produto = input('Digite o produto: ')
        preco = float(input('Digite o preco do produto: '))
        precos[produto] = preco
        print(f'Produto {produto} adicionado com sucesso')
    print(f'Segue Planilha atualizada\n {precos}')

print('---- atualização dos valores do produto -----')
 """
precos_novos = {}
for item_produto, item_preco in precos.items():
    if item_preco <= 1000:
        item_preco *= 1.1
        precos_novos[item_produto] = item_preco
        print(f'{item_produto} teve aumento de 10%, e ficou {item_preco} o total')
    elif item_preco >1000 and item_preco <= 2000:
        item_preco *=1.15
        precos_novos[item_produto] = item_preco
        print(f'{item_produto} teve aumento de 15%, e ficou {item_preco} o total')
    elif item_preco > 2000:
        item_preco *= 1.20
        precos_novos[item_produto] = item_preco
        print(f'{item_produto} teve aumento de 20%, e ficou {item_preco} o total')
    
    
print(f'Tabela comparativa:\n {precos}')

print(f'Tabela comparativa:\n {precos_novos}')





        
    