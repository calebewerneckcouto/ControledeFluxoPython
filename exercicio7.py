'''O jogo “Acerte o número” funciona da seguinte maneira:
a. Existe um certo número inteiro declarado dentro do programa que o usuário
desconhece. Por exemplo: numero = 8
b. O usuário tem 3 tentativas para acertar o número.
c. A cada tentativa, é informado ao usuário se o número que ele digitou é maior,
menor, ou igual ao número correto.
d. O jogo termina quando o usuário erra 3 vezes (perdeu) ou quando o usuário
acerta o número (ganhou).
Implemente o jogo “Acerte o número”.'''


# Número secreto
s = 10  

# Contador de tentativas
contador = 3  

# Laço de tentativas
while contador > 0:
    # Solicita um número ao usuário
    n = int(input("Informe um número: "))

    # Verifica se o número está correto
    if n == s:
        print("Parabéns! Você acertou o número secreto!")
        break
    elif n > s:
        print("O número que você digitou é maior que o número secreto.")
    else:
        print("O número que você digitou é menor que o número secreto.")

    # Decrementa o contador
    contador -= 1

    # Verifica se acabou as tentativas
    if contador == 0:
        print("Acabaram suas jogadas. Você perdeu!")

        
        