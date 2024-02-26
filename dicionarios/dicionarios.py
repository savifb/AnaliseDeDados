dicionario = {}

dicionario['Produto']: 5000

dicionario.update({'Iphone': 213132, 'Boneca': 31321}) 

print(dicionario)
del dicionario['Iphone']

print(dicionario)

boneca = dicionario.pop('Boneca')

print(dicionario)
print(boneca)

dicionario.clear()

print(dicionario)
