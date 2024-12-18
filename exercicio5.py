'''Escreva um programa que receba um número inteiro n e imprima todos os
números pares de 1 até n (inclusive n )'''

n = int(input("Informe um número: "))


for i in range(1, n + 1):
    if i % 2 ==0:
        print(i)


