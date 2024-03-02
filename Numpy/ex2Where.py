import numpy as np

salarios = np.array([3000, 2500, 3500, 4000, 2000, 4500, 3000, 3800, 4800])

media_salarios = np.mean(salarios)

print(round(media_salarios,2))

qtd_maiorMedia = len(salarios[(salarios >= media_salarios)])

print(qtd_maiorMedia)

print(np.sum(salarios >= media_salarios)) #true significa 1 e false significa 0 (você somou os 1)
