meta = 23000

vendas = [
    ('João', 15000),
    ('Julia', 20000),
    ('Marcus', 30000),
    ('Maria', 35000),
    ('Ana', 20000),
    ('Alon', 1500),
    
]
for vendedor, qtd in vendas: 
    if qtd <= meta:
        print(qtd)
