def adicionar_item(lista_produtos):
    produto = input('Digite o Produto a ser adicionado: ')
    produto = produto.upper()
    produto = produto.replace(" ", "")
    if produto not in lista_produtos:
        lista_produtos.append(produto)
    else:
        print('Produto já é contido na lista')
    return lista_produtos

def remove_item(lista_produtos):
    produto =  input('Digite o Produto a ser removido: ')
    produto = produto.upper()
    produto = produto.replace(" ", "")
    if produto in lista_produtos:
        lista_produtos.remove(produto)
    else:
        print('Produto não encontrado')
    return lista_produtos

def ver_lista(lista_produtos):
    for item in lista_produtos:
        print(item)
    return lista_produtos


def opcoes_de_acao(decisao):
    if decisao == 1: 
        #adicionar item
        adicionar_item(lista)
    elif decisao == 2:
        #remover item
        remove_item(lista)

    elif decisao == 3:
        #mostrar item
        print(ver_lista(lista))
    
        #sair do programa
lista = []
while True:
    decisao = int(input('1 - Adicionar Item\n2 - Remover Item\n3 - Visualizar Itens\n4- Sair do Programa\n'))
    if decisao == 4:
        print('Saindo do Programa')
        break
    opcoes_de_acao(decisao)




print(lista)
