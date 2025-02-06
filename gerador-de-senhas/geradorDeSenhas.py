
"""
Objetivo:
Criar um programa que gere senhas aleatórias com um comprimento definido pelo usuário
"""

import random
import string


def gerar_senha(tamanho=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.SystemRandom().choice(caracteres) for _ in range(tamanho))
    return senha


#interação com o usuário
try:
    tamanho = int(input("Digite o tamanho da senha: "))
    if tamanho <= 0:
        print("Tamanho deve ser um número positivo!")
    else:
        print(f"Senha gerada: {gerar_senha(tamanho)}")
except ValueError:
    print("Por favor, insira um número valido!")
