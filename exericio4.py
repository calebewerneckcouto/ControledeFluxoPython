'''Escreva um programa que receba um número inteiro n e imprima a soma de todos
os números de 1 até n (inclusive n ).'''


soma = 0


n = int(input("Informe um número: "))


for i in range(1, n + 1):
    soma += i

print(f"A soma de todos os números de 1 até {n} é: {soma}")

