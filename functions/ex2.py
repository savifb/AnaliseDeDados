def calc_tributo(preco, custo, lucro):
    delta = preco - custo
    tributo = ((delta-lucro)*100)/preco
    return tributo

preco = 1500
custo = 400
lucro = 800

print(f'O tributo com o preço: {preco}, custo: {custo} e lucro: {lucro} é de: {calc_tributo(preco,custo,lucro)}%') 