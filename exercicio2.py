'''Implemente uma calculadora que recebe 3 valores do usuário:
a. Operando a (pode ser um inteiro ou float).
b. Operando b (pode ser um inteiro ou float).
c. Operador op .
i. op pode ser uma string representando o operador, por exemplo, "+" ou "-
". Outra opção é utilizar números, por exemplo, 1 para soma , 2 para
subtração , etc.
O seu programa deve receber esses 3 valores e imprimir o resultado da operação.
Caso o operador seja de divisão e o segundo operando seja o valor zero, o
programa deve imprimir uma mensagem: “Não é possível realizar divisão por
zero!”.'''



a = float(input("Informe o primeiro valor (inteiro ou float): "))
b = float(input("Informe o segundo valor (inteiro ou float): "))

op = input("Escolha a operação a ser realizada (+, -, /, *): ")

if op == '+':
    print(f"Resultado: {a + b}")
elif op == '-':
    print(f"Resultado: {a - b}")
elif op == '/':
    if b == 0:
        print("Não é possível realizar divisão por zero!")
    else:
        print(f"Resultado: {a / b}")
elif op == '*':
    print(f"Resultado: {a * b}")
else:
    print("Operador inválido!")
