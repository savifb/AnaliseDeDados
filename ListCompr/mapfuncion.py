def padroniza_texto(lista):
    lista = lista.casefold()
    lista = lista.replace("  ", " ")
    lista = lista.strip()
    return lista

produtos = [' ABC12 ', 'abc34', 'AbC37', 'beb12', ' BSA151', 'BEB23']
print(produtos)
print('---------------------')
for i, produto in enumerate(produtos):
    produtos[i] = padroniza_texto(produto)

print(produtos)
print('------------------------')
list_map = list(map(padroniza_texto, produtos))
print(list_map)