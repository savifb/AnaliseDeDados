def adiciona_produto(dicionario):
    produto = input('Digite o produto que deseja adicionar: ')
    produto = produto.upper()
    produto = produto.replace(" ", '')
    if produto not in dicionario:
        qtd_produto = int(input(f'Digite a quantidade de {produto} que deseja adicionar: '))
        dicionario[produto] = qtd_produto
    else:
        print('Produto já contido na lista1')
    return dicionario


def remove_produto(dicionario):
    produto = input('Digite o produto que deseja excluir: ')
    produto = produto.upper()
    produto = produto.replace(" ", '')
    if produto in dicionario:
        del dicionario[produto]
    else:
        print(f'{produto} não encontrado, tente novamente')
    return dicionario

def ver_lista(dicionario):
    for item, qtd in dicionario.items():
        print(f'{item} possui {qtd} quantidades')


def decisao_escolhida(decisao):
    if decisao == 1:
        adiciona_produto(produtos)
    elif decisao == 2:
        remove_produto(produtos)
    elif decisao == 3:
        ver_lista(produtos)
produtos = {}
while True:
    decisao = int(input('1 - ADICIONAR PRODUTO\n 2 - REMOVE PRODUTO\n 3 - VISUALIZA PRODUTOS\n 4 - SAIR DO PROGRAMA\n'))
    if decisao == 4:
        print(produtos)
        break
    else:
        decisao_escolhida(decisao)