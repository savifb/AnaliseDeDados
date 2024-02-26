vendas_22 = {"jan": 15000, "fev": 15500, "mar": 14000, "abr": 16600, "mai": 16300, "jun": 17000}
vendas_23 = {"jan": 17000, "fev": 15000, "mar": 17500, "abr": 16900, "mai": 16000, "jun": 18500}
crescimento_total = 0 
""" for mes, valor in vendas_22.items():
    for mes23, valor23 in vendas_23.items():
        if mes == mes23:
            delta = valor23 - valor
            crescimento = ((delta)/valor)*100
            crescimento_total+=crescimento
            if crescimento > 0:
                print( f'Houve crescimento do {mes23}/23  em relação ao {mes}/22 de {crescimento:.2f} % ')
            else:
                print(f'Houve decrescimo do {mes23} em relação ao {mes} de {crescimento:.2f} %')

print(F'O Crescimento de 2023 em relação a 2022 foi de {crescimento_total:.2f} %')
 """
print('----- CASO DESSE EMPATADO ----')

for mes, valor in vendas_22.items():
    for mes23, valor23 in vendas_23.items():
        if mes == mes23:
            delta = valor23 - valor
            crescimento = ((delta)/valor)*100
            if crescimento > 0:
                print( f'Houve crescimento do {mes23}/23  em relação ao {mes}/22 de {crescimento:.2f} % ')
            if crescimento <= 0: 
                valor = valor23
                delta = valor23 - valor
                crescimento = ((delta)/valor)*100
                print( f'Houve crescimento do {mes23}/23  em relação ao {mes}/22 de {crescimento:.2f} % ')
            crescimento_total+=crescimento

print(F'O Crescimento de 2023 em relação a 2022 foi de {(crescimento_total/len(vendas_23) - 1):.2f} %')
