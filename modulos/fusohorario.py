from datetime import datetime
import pytz

data_hora_atual = datetime.now()    

fuso_sp = pytz.timezone('America/Sao_Paulo')
fuso_ny = pytz.timezone('America/New_York')
fuso_toquio = pytz.timezone('Asia/Tokyo')

hora_fuso_sp = data_hora_atual.astimezone(fuso_sp)
hora_fuso_ny = data_hora_atual.astimezone(fuso_ny)
hora_fuso_toquio = data_hora_atual.astimezone(fuso_toquio)

print(f'SP:  {hora_fuso_sp}\n, Ny: {hora_fuso_ny}\n, Toquio:  {hora_fuso_toquio}\n')