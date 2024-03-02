import numpy as np

# Crie um gerador de números aleatórios.
rng = np.random.default_rng()

numero_aleatorio = rng.random()
print(numero_aleatorio)

rng_array = np.random.default_rng(seed=0)

array_aleatorio = rng_array.random(3)

print(array_aleatorio)

print('------------------------')
rng_array = np.random.default_rng(seed=0)
dados_vendas_ficticios = rng_array.integers(low=50, high=250, size=30)
print(dados_vendas_ficticios)

dia_valormaximo = np.argmax(dados_vendas_ficticios)+1
dia_valorminimo = np.argmin(dados_vendas_ficticios)+1

print(f'Dia do valor máximo: {dia_valormaximo}')
print(f'Dia do valor mínimo: {dia_valorminimo}')

print('---------------------------')

media_vendas = np.mean(dados_vendas_ficticios)
print(f'Media de vendas: {media_vendas}')
mediana = np.median(dados_vendas_ficticios)
print(mediana)
percentual = np.percentile(dados_vendas_ficticios, 25)
print(percentual)
desvio_padrao = np.std(dados_vendas_ficticios)
print(desvio_padrao)
print(desvio_padrao**2)
varianca = np.var(dados_vendas_ficticios)
print(varianca )