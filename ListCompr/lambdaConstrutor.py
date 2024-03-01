def calcula_imposto(imposto):
    return lambda preco: preco * (1 + imposto)

calcular_imposto_royalties = calcula_imposto(0.15)
calcular_imposto_servico = calcula_imposto(0.10)
calcular_imposto_venda = calcula_imposto(0.05)

print(calcular_imposto_royalties(100))
print(calcular_imposto_servico(150))
print(calcular_imposto_venda(200))