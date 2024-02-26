vendas_tecnologia = {'notebook asus': 2450, 'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'notebook dell': 17000, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000}

item_vendas = vendas_tecnologia.items()

print(item_vendas)

for produtos, qtd in vendas_tecnologia.items():
    if qtd > 5000:
        print(f'{produtos} vendeu {qtd} unidades\n E atingiu a meta')
    else:
        print(f'{produtos} Não atingiu a meta, \n E vendeu {qtd} unidades')
print('---------------------------------')

chaves = vendas_tecnologia.keys()
valores = vendas_tecnologia.values()

lista_chaves = list(chaves)
lista_chaves.sort()
lista_valores =  list(valores)

print('Essas são minhas chaves {} '.format(lista_chaves))
print('Esses são meus valores {}'.format(lista_valores)) 


print('-----------------------------------------')

dicionario_chaves = dict.fromkeys(lista_chaves, 0)

print(dicionario_chaves)

lista_tuplas = zip(chaves, valores)

print(lista_tuplas)

dicionarioDasTuplas = dict(lista_tuplas)

print(dicionarioDasTuplas)

#OU

for item in lista_tuplas:
    print(item)



