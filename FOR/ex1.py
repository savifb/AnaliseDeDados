qtd_pessoas = int(input("Digite a quantdade de Pessoas que vai ter no quarto: "))
quarto = []
if qtd_pessoas <= 4:          
    for i in range(qtd_pessoas):
        nome = input("Digite seu nome: ")
        cpf = input("Digite seu CPF:")
        hospede = [nome,cpf]
        quarto.append(hospede)
elif qtd_pessoas <=0:
    print("quantidade inexistente")
else:
    print('Quarto Lotado')



print(quarto)

