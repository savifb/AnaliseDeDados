mes = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto','setembro', 'outubro', 'novembro', 'dezembro']
vendas_1sem = [500, 1000, 4000, 2300, 3883, 9000]
vendas_2sem = [300, 250, 900, 1000, 1200, 3000]

vendas_1sem.extend(vendas_2sem)

maior_valor = max(vendas_1sem)
index_maior_valor = vendas_1sem.index(maior_valor)
menor_valor = min(vendas_1sem)
index_menor_valor = vendas_1sem.index(menor_valor)

print(maior_valor)

print(f'A maior venda foi de: {maior_valor} referente ao mês de {mes[index_maior_valor]}')
print(f'A menor venda foi de: {menor_valor} referente ao mês de {mes[index_menor_valor]}')

faturamento_total = sum(vendas_1sem)

print(f'O faturamento total foi de: {faturamento_total}')
