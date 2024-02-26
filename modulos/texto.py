import string 
from collections import Counter

texto = input('Digite a frase: ')

def analisar_texto(texto):
    palavras = texto.split()
    qtd_palavras = len(palavras)
    frequencia_palavras = Counter(palavras)
    frequencia_letras = Counter(texto)
    return qtd_palavras, frequencia_palavras, frequencia_letras

qtd_palavras, frequencia_palavras, frequencia_letras = analisar_texto(texto)

print(f'Contagem de palavras: {qtd_palavras}')
print(f'frequencia de palavras: {frequencia_palavras}')
print(f'frequencia de letras:  {frequencia_letras}')