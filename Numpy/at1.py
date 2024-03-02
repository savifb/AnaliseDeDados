import numpy as np
import time

lista = list(range(1, 10_000_001))
array = np.array(range(1, 10_000_001))

inicio = time.time()
soma_lista = sum(lista)
fim = time.time()
print(f'Tempo para somar os numero na lista = {fim-inicio}')

inicio2 = time.time()
soma_awway = np.sum(array)
fim2 = time.time()
print(f'Tempo para somar os números do np = {fim2-inicio2}')
