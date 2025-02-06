
"""
riando uma tupla com números pares
Crie uma tupla contendo os números pares de 0 a 20 e faça:

1 - Exiba os cinco primeiros números da tupla.
2 - Exiba os cinco últimos números da tupla.
3 - Exiba a tupla ao contrário.
"""

#Criando tupla com números pares
pares = tuple(range(0, 21, 2))
print(pares, "\n")

#Exibindo os cinco primeiros elementos
print(f"Cinco primeiros elementos: {pares[:5]}")
print(f"Cinco últimos elementos: {pares[5:]}")
print(f"Tupla ao contrário: {pares[::-1]}")
