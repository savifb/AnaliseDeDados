import numpy as np

# Preços dos produtos
precos = np.array([20, 25, 30, 35, 40])

# Aumentar os preços em 10 % (ex.: ajuste de inflação)
print(precos)
novos_precos = precos*1.1

print(novos_precos)


# Vendas do dia
vendas = np.array([200, 220, 250, 210, 300])

# Somar todas as vendas

total1 = sum(vendas)
total2= np.sum(vendas)

print(total1)
print(total2)



medias = np.mean(vendas)

print(medias)

maximo = np.max(vendas)
minimo = np.min(vendas)

print(f'Produto mais caro {maximo}')
print(f'Produto mais barato {minimo}')

vendas_ordenadas = np.sort(vendas)

print(vendas_ordenadas)

import numpy as np

# Número de produtos vendidos
quantidades = np.array([10, 20, 30, 40])

# Preços dos produtos
precos = np.array([5, 10, 15, 20])

# Calcular o valor total de vendas?

valor_total1 = np.sum(precos*quantidades)
print(valor_total1)
valor_total2 = np.dot(precos,quantidades)
print(valor_total2)