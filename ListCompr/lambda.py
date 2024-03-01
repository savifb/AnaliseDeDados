imposto = 0.3
def minha_funcao1(num):
    return num*(1+imposto)

minha_funcao = lambda num : (num*(1+imposto))

print(minha_funcao1(1000))
print(minha_funcao(1000))