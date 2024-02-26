produtos = ['computador', 'livro', 'celular', 'tv', 'ar condicionado','alexa', 'maquina de cafe', 'kindle']
vendas2019 = [100, 250, 300, 150, 100, 200, 50, 250]
vendas2020 = [200, 46, 78, 90, 150, 250, 789, 300]

for i,  item in enumerate(produtos):
     if vendas2020[i] > vendas2019[i]:
          print(produtos[i])