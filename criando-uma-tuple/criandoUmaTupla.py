

"""
Criando uma tupla a partir do usuário
Peça ao usuário para digitar 5 números e armazene-os em uma tupla. Depois, exiba:

A soma de todos os números.
A média dos valores.
"""

numeros = tuple(map(int, input("Digite 5 números separado por espaço: ").split()))

soma = sum(numeros)
media = soma / len(numeros)

print(f"A soma dos números: {soma}")
print(f"A média dos números: {media}")
