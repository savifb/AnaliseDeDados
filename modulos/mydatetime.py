from datetime import datetime

data_compra_anterior = datetime(2023, 5, 10)

print(data_compra_anterior)

data_hora_atual = datetime.now()

print(data_hora_atual)

data_diferencial = data_hora_atual - data_compra_anterior

print(data_diferencial)

print(data_diferencial.days)

if data_diferencial.days >=  100:
    print('Parabens voce ganhou cupom')