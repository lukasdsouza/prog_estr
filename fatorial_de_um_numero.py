import math

def fatorial(n):
    return math.factorial(n)

num = int(input("Digite um número inteiro positivo: "))
if num < 0:
    print("Entrada inválida! Por favor, insira um número inteiro positivo.")
else:
    print(f"O fatorial de {num} é: {fatorial(num)}")