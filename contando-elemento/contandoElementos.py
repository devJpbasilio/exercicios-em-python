"""
Exercício 2: Contando elementos
Dada a tupla:
numeros = (2, 4, 6, 8, 2, 10, 2, 4)


1 - Conte quantas vezes o número 2 aparece na tupla.
2 - Descubra o índice da primeira ocorrência do número 6.
"""

numeros = (2, 4, 6, 8, 2, 10, 2, 4)

quantidade = numeros.count(2)
print(f"Quantidade de vezes em que o número 2 aparece: {quantidade}x")

print("\n")
indice = numeros.index(6)
print(f"O número 6 aparece pela primeira vez no índice {indice}.")

